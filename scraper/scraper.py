import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.visited = set()
        self.pages = []

    def is_internal(self, url):
        return url.startswith(self.base_url)

    def get_links(self, soup, current_url):
        links = set()
        for a in soup.find_all("a", href=True):
            full_url = urljoin(current_url, a["href"].split('#')[0])
            if self.is_internal(full_url):
                links.add(full_url)
        return links

    def scrape(self):
        to_visit = {self.base_url}
        while to_visit:
            url = to_visit.pop()
            if url in self.visited:
                continue
            try:
                res = requests.get(url, timeout=10)
                if res.status_code == 200 and 'text/html' in res.headers["Content-Type"]:
                    soup = BeautifulSoup(res.text, "html.parser")

                    for tag in soup(["nav", "footer", "header", "script", "style"]):
                        tag.decompose()

                    html = soup.prettify()
                    self.pages.append(html)

                    print(f"[+] Scraped: {url}")
                    new_links = self.get_links(soup, url)
                    to_visit.update(new_links - self.visited)

                self.visited.add(url)
                time.sleep(0.5)
            except Exception as e:
                print(f"[!] Failed: {url} ({e})")

        return self.pages
