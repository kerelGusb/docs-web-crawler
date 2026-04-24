import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class MarkdownBuilder:
    def __init__(self, project_dir, output_file="docs.md"):
        self.project_dir = project_dir
        self.output_file = output_file
        self.visited = set()

    def build(self, root):
        pages = self._collect_bfs(root)

        with open(self.output_file, "w", encoding="utf-8") as f:
            for url in pages:
                if url in self.visited:
                    continue
                self.visited.add(url)

                html = self._load_html(url)
                if not html:
                    continue

                html = self._preprocess(html)

                markdown = md(
                    html,
                    heading_style="ATX",
                    bullets="*",
                    tables=True
                )
                f.write(markdown)
                f.write("\n\n---\n")

        print(f"[MarkdownBuilder] saved -> {self.output_file}")

    def _collect_bfs(self, root):
        queue = [root]
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node.url)

            for child in node.children:
                queue.append(child)

        return order

    def _load_html(self, url):
        filename = self._filename(url) + ".html"
        path = os.path.join(self.project_dir, "html", filename)

        if not os.path.exists(path):
            print(f"[WARN] missing html: {path}")
            return None

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _filename(self, url):
        path = urlparse(url).path.strip("/")

        if not path:
            return "index"

        return path.replace("/", "_")

    def _extract_content(self, soup):
        selectors = [
            "div#documentation-content"
            "td.content",
            "main#bodyColumn",
            "main",
            "article",
            "page-content"
            "div#contentBox",
            "div#bodyColumn",
            "div#content",
            "main-body",
            '[class*="docItemContainer"]',
            '[class*="content"]'
        ]

        for sel in selectors:
            el = soup.select_one(sel)

            if el:
                if el.name == "td":
                    return BeautifulSoup(el.decode_contents(), "lxml")

                return el
    
        if soup.body:
            return soup.body

        return soup

    def _preprocess(self, html):
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        for tag in soup.select("nav, navbar, header, footer, aside"):
            tag.decompose()

        content = self._extract_content(soup)

        for tag in content.select("nav, aside, .sidebar, .toc, .navigation"):
            tag.decompose()

        for img in soup.find_all("img"):
            src = img.get("src")
            if src and not src.startswith("http"):
                continue

        return str(content)