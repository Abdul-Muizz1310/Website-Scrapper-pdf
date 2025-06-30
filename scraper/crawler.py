import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://javascript.info"

def get_internal_links(url, visited=None):
    if visited is None:
        visited = set()

    links_to_visit = [url]
    all_links = set()

    while links_to_visit:
        current = links_to_visit.pop()
        if current in visited:
            continue
        visited.add(current)
        try:
            response = requests.get(current, timeout=10)
        except Exception:
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag['href']
            if href.startswith('#') or 'mailto:' in href:
                continue
            full_url = urljoin(current, href)
            if BASE_URL in full_url and full_url not in visited:
                links_to_visit.append(full_url)
                all_links.add(full_url)

    return sorted(all_links)
