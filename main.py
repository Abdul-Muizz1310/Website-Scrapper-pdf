from scraper.crawler import get_internal_links
from scraper.merger import merge_all_to_single_html
from playwright.sync_api import sync_playwright
import os

def main():
    base_url = "https://javascript.info"
    print("🔍 Crawling all internal links...")
    links = get_internal_links(base_url)
    print(f"🔗 Found {len(links)} pages")

    merged_html_path = "output/merged.html"
    merge_all_to_single_html(links, merged_html_path)

    print("📄 Generating final PDF...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file:///{os.path.abspath(merged_html_path)}", wait_until="load")
        page.pdf(path="output/javascript_info_full.pdf", format="A4", print_background=True)
        browser.close()

    print("✅ PDF generated at output/javascript_info_full.pdf")

if __name__ == "__main__":
    main()
