import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import warnings
from bs4 import XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


class Node:
    def __init__(self, url):
        self.url = url
        self.children = []


class LinkTree:
    def __init__(self, start_url, max_pages=300, debug=False):
        self.start_url = start_url
        self.max_pages = max_pages
        self.debug = debug

        parsed = urlparse(start_url)
        self.domain = parsed.netloc

        self.base_path = parsed.path or "/"

        if not self.base_path.endswith("/"):
            self.base_path = self.base_path.rsplit("/", 1)[0] + "/"

        self.session = requests.Session()

        self.root = None
        self.visited = set()

        print(f"[LinkTree] start: {start_url}")
        print(f"[LinkTree] scope: {self.domain}{self.base_path}")
        print(f"[LinkTree] max_pages: {max_pages}")

    def build(self):
        root_url = self._normalize_url(self.start_url)
        self.root = Node(root_url)

        queue = deque([self.root])
        self.visited = {root_url}

        processed = 0

        while queue and len(self.visited) < self.max_pages:
            current_node = queue.popleft()
            processed += 1

            if processed % 10 == 0:
                print(f"[LinkTree] processed: {processed}, visited: {len(self.visited)}")

            if self.debug:
                print(f"[DEBUG] parsing {current_node.url}")

            links = self._get_links(current_node.url)

            for link in links:
                if link in self.visited:
                    continue

                self.visited.add(link)

                child = Node(link)
                current_node.children.append(child)
                queue.append(child)

        print(f"[LinkTree] done: {len(self.visited)} pages collected")
        return self.root

    def _normalize_url(self, url):
        parsed = urlparse(url)

        path = parsed.path

        if path.endswith("/index.html"):
            path = path[:-10]

        return f"{parsed.scheme}://{parsed.netloc}{path}"

    def _in_scope(self, url):
        parsed = urlparse(url)

        if parsed.netloc != self.domain:
            return False

        return parsed.path.startswith(self.base_path)

    def _get_links(self, url):
        try:
            response = self.session.get(url, timeout=5)

            content_type = response.headers.get("Content-Type", "").lower()
            if "text/html" not in content_type:
                return []

            soup = BeautifulSoup(response.text, "html.parser")

            links = set()

            for a in soup.find_all("a", href=True):
                full_url = urljoin(url, a["href"])
                clean_url = self._normalize_url(full_url)

                if not self._in_scope(clean_url):
                    continue

                links.add(clean_url)

            return list(links)

        except Exception:
            return []