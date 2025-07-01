import os
import re
from urllib.parse import urlparse
from scraper.crawler import get_internal_links
from playwright.sync_api import sync_playwright

def sanitize_filename_from_url(url):
    path = urlparse(url).path.strip('/')
    if not path:
        return "index"
    # Remove trailing slashes and replace non-word characters
    return re.sub(r'[\\/*?:"<>|]', '', path.replace('/', '_'))

def generate_clean_pdf(url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"🧹 Processing {url}")

        try:
            page.goto(url, timeout=20000, wait_until="domcontentloaded")
        except Exception as e:
            print(f"❌ Failed to load {url}: {e}")
            browser.close()
            return

        # Remove nav/comments/links/images
        page.evaluate("""
            () => {
                const selectorsToRemove = [
                    'nav', 'header', 'footer',
                    '.top-nav', '.comments', '.comment', '.comment-thread', '.disqus-thread'
                ];
                selectorsToRemove.forEach(selector => {
                    document.querySelectorAll(selector).forEach(el => el.remove());
                });

                // Remove links (keep text)
                document.querySelectorAll('a').forEach(a => {
                    const span = document.createElement('span');
                    span.textContent = a.textContent;
                    a.replaceWith(span);
                });

                // Remove images and other visuals
                document.querySelectorAll('img, svg, picture, video').forEach(el => el.remove());
            }
        """)

        # Only keep the article body
        article_html = page.evaluate("""
            () => {
                const article = document.querySelector('[itemprop="articleBody"]');
                if (!article) return '';
                const html = `<html><head><meta charset='utf-8'></head><body>${article.outerHTML}</body></html>`;
                return html;
            }
        """)

        if not article_html.strip():
            print(f"⚠️ Skipping {url} — no articleBody found.")
            browser.close()
            return

        # Load this article content into a new page for PDF generation
        page = browser.new_page()
        page.set_content(article_html, wait_until="domcontentloaded")

        filename = sanitize_filename_from_url(url) + ".pdf"
        pdf_path = os.path.join(output_dir, filename)

        page.pdf(path=pdf_path, format="A4", print_background=True)
        print(f"✅ Saved: {pdf_path}")
        browser.close()
