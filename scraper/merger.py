import os
from playwright.sync_api import sync_playwright
from scraper.crawler import get_internal_links

def clean_and_extract_body(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        page.evaluate("""
            () => {
                const comments = document.querySelectorAll('.comments, .comment, .comment-thread, .disqus-thread');
                comments.forEach(el => el.remove());
            }
        """)

        html = page.content()
        browser.close()
        return html

def merge_all_to_single_html(links, output_html_path):
    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)

    merged_html = ['<html><head><meta charset="utf-8"></head><body>']
    for i, url in enumerate(links):
        print(f"Processing {i+1}/{len(links)}: {url}")
        try:
            content = clean_and_extract_body(url)
            body_start = content.find("<body")
            body_content = content[body_start:]
            merged_html.append(f"<section>{body_content}</section><hr style='margin:50px 0;'>")
        except Exception as e:
            print(f"Failed: {e}")
            continue
    merged_html.append("</body></html>")

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(merged_html))

    print(f"Merged HTML saved at {output_html_path}")
