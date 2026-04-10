import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from doc_tree_crawler import build_tree
from urllib.parse import urljoin, urlparse

BASE_URL = "https://commons.apache.org/proper/commons-codec/project-info.html"
OUTPUT_MD = "docs.md"
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)


def download_html(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.text

def download_image(src, base_url):
    if src.startswith("data:image"):
        header, encoded = src.split(",", 1)
        ext = header.split("/")[1].split(";")[0]
        filename = f"img_{hash(src)}.{ext}"
        path = os.path.join(IMAGES_DIR, filename)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(base64.b64decode(encoded))
        return path
    else:
        img_url = urljoin(base_url, src)
        filename = os.path.basename(img_url.split("?")[0])
        path = os.path.join(IMAGES_DIR, filename)
        if not os.path.exists(path):
            r = requests.get(img_url)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
        return path


def extract_content(soup):
    selectors = [
        "td.content",
        "main#bodyColumn",
        "main",
        "article",
        "div#contentBox",
        "div#bodyColumn",
        "div#content",
    ]

    for sel in selectors:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 200:
            return el

    return soup.body or soup


def preprocess_html(html, base_url):
    html = html.replace("\u00A0", " ")

    soup = BeautifulSoup(html, "xml")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    for tag in soup.select("nav, header, footer, aside"):
        tag.decompose()

    content = extract_content(soup)

    for tag in content.select("nav, aside, .sidebar, .toc, .navigation"):
        tag.decompose()

    for img in content.find_all("img"):
        src = img.get("src")
        if src:
            img["src"] = download_image(src, base_url)
    
    for table in content.find_all("table"):
        table.unwrap()

    for tag in content.find_all(["tr", "li", "p", "h1", "h2", "h3"]):
        tag.insert_after("\n")

    return str(content)


def html_to_markdown(html):
    return md(html, heading_style="ATX", bullets="*")


def collect_bfs_nodes(root):
    queue = [root]
    order = []

    while queue:
        node = queue.pop(0)
        order.append(node.url)

        for child in node.children:
            queue.append(child)

    return order


def main():
    tree = build_tree(BASE_URL, max_pages=5)

    urls = collect_bfs_nodes(tree)

    visited = set()

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        for i, url in enumerate(urls, 1):

            if url in visited:
                continue
            visited.add(url)

            print(f"parsing {url}...")

            try:
                html = download_html(url)
                html = preprocess_html(html, url)
                page_md = html_to_markdown(html)

                f.write(page_md)
                f.write("\n\n---\n")

            except Exception as e:
                print(f"error: {url}: {e}")


if __name__ == "__main__":
    main()