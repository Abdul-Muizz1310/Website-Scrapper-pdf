import sys
from scraper.scraper import WebScraper
from scraper.pdf_generator import PDFGenerator

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python main.py <website_url>")
        return

    url = sys.argv[1]
    print(f"🌐 Starting scrape on: {url}")
    scraper = WebScraper(url)
    pages = scraper.scrape()

    if pages:
        pdf_gen = PDFGenerator(pages)
        pdf_gen.create_pdf("website_output.pdf")
    else:
        print("⚠️ No pages scraped.")

if __name__ == "__main__":
    main()
