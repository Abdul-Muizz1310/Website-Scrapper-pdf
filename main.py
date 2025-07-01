from scraper.crawler import get_internal_links
from scraper.merger import generate_clean_pdf

def main():
    base_url = "https://javascript.info"
    print("🔍 Crawling all internal links...")
    links = get_internal_links(base_url)

    # Optional: limit for testing
    #links = links[:10]

    print(f"🔗 {len(links)} links found. Generating individual PDFs...")
    for link in links:
        try:
            generate_clean_pdf(link, "output")
        except Exception as e:
            print(f"❌ Error generating PDF for {link}: {e}")

if __name__ == "__main__":
    main()
