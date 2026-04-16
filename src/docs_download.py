import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

class Downloader:
    def __init__(
        self,
        timeout = 10,
        retries = 3,
        user_agent = "Mozilla/5.0"
    ):
        self.timeout = timeout
        self.retries = retries

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent
        })

        self._cache: dict[str, bytes] = {}

    def download_file(self, url, path):
        try:
            content = self.get(url)
        except Exception as e:
            print(f"[WARN] skip asset: {url} ({e})")
            return

        try:
            with open(path, "wb") as f:
                f.write(content)
        except Exception as e:
            print(f"[WARN] cannot save file {path}: {e}")

    def get(self, url):
        if url in self._cache:
            return self._cache[url]

        last_error = None

        for _ in range(self.retries):
            try:
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()

                content = response.content
                self._cache[url] = content
                return content

            except Exception as e:
                last_error = e

        print(f"[WARN] failed download: {url} ({last_error})")
        return None


class DocsDownload:
    def __init__(self, link_tree, downloader, output_dir="output"):
        self.tree = link_tree
        self.downloader = downloader

        self.output_dir = output_dir
        self.project_dir = None

        self.html_dir = None

        self.visited_pages = set()
        self.downloaded_assets = set()

    def run(self):
        root = self.tree.build()

        self.project_dir = self._infer_project_name(root.url)
        self.project_dir = os.path.join(self.output_dir, self.project_dir)

        self.html_dir = os.path.join(self.project_dir, "html")
        assets_dir = os.path.join(self.project_dir, "assets")

        os.makedirs(self.project_dir, exist_ok=True)
        os.makedirs(self.html_dir, exist_ok=True)
        os.makedirs(assets_dir, exist_ok=True)
        

        queue = [root]

        print(f"[DocsDownload] project: {self.project_dir}")

        while queue:
            node = queue.pop(0)

            if node.url in self.visited_pages:
                continue

            self.visited_pages.add(node.url)

            print(f"[DocsDownload] page: {node.url}")

            html_bytes = self.downloader.get(node.url)

            if not html_bytes:
                print(f"[WARN] skip page (download failed): {node.url}")
                continue

            html = html_bytes.decode("utf-8", errors="ignore")

            html = self._process_images(html, node.url)

            self._save_page(node.url, html)

            queue.extend(node.children)

        print(f"[DocsDownload] done")

    def _process_images(self, html, page_url):
        soup = BeautifulSoup(html, "html.parser")

        for img in soup.find_all("img", src=True):
            img_url = urljoin(page_url, img["src"])

            if img_url in self.downloaded_assets:
                continue

            self.downloaded_assets.add(img_url)

            filename = self._filename(img_url)
            local_path = f"assets/{filename}"
            full_path = os.path.join(self.project_dir, local_path)

            self.downloader.download_file(img_url, full_path)

            img["src"] = local_path

        return str(soup)

    def _save_page(self, url, html):
        filename = self._filename(url) + ".html"
        path = os.path.join(self.html_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

    def _filename(self, url):
        path = urlparse(url).path.strip("/")

        if not path:
            return "index"

        return path.replace("/", "_")

    def _infer_project_name(self, url):
        parsed = urlparse(url)

        netloc = parsed.netloc.replace("www.", "")

        path = parsed.path

        if path.endswith((".html", ".htm")):
            path = path.rsplit("/", 1)[0]

        parts = [netloc] + [p for p in path.split("/") if p]

        if len(parts) == 1:
            return parts[0].replace(".", "_")

        return "_".join(parts).replace(".", "_")