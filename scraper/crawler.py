import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://javascript.info"

def get_internal_links(url, visited=None):
    if visited is None:
        visited = set()

    links_to_visit = [url]
    all_links = set()

    UNWANTED_PATHS = [
    "/blob", "/rss", "/sitemap", "/search", "/favicon", 
    "/contributors", "/about", "/article/contributors",
    "/ebook","/rss", "/sitemap", ".xml", ".json","/article",
    "/task","/tutorial"
    ]

    while links_to_visit:
        current = links_to_visit.pop()
        if current in visited:
            continue
        visited.add(current)
        try:
            response = requests.get(current, timeout=10)
            content_type = response.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                print(f"❌ Skipping non-HTML content: {current} ({content_type})")
                continue

            print(f"Currently crawling: {current}")

        except Exception as e:
            print(f"⚠️ Request failed for {current}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for a_tag in soup.find_all("a", href=True):
            href = a_tag['href']
             # Skip anchor links or mailto
            if href.startswith('#') or 'mailto:' in href:
                continue

            full_url = urljoin(current, href)

            # Only allow internal links
            if not full_url.startswith(BASE_URL):
                continue

            # Skip unwanted extensions
            if any(full_url.endswith(ext) for ext in [".pdf", ".jpg", ".jpeg", ".png", ".gif", ".zip", ".rar", ".ico", ".svg"]):
                continue

            # Skip unwanted paths
            if any(bad in full_url for bad in UNWANTED_PATHS):
                continue

            if full_url not in visited:
                links_to_visit.append(full_url)
                all_links.add(full_url)

    return sorted(all_links)
