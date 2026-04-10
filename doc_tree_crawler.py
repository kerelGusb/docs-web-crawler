import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import os


class Node:
    def __init__(self, url):
        self.url = url
        self.children = []


def normalize_url(url):
    parsed = urlparse(url)

    path = parsed.path

    if path.endswith("/index.html"):
        path = path[:-11]

    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")

    return f"{parsed.scheme}://{parsed.netloc}{path}"


def get_base_path(start_url):
    parsed = urlparse(start_url)
    path = parsed.path

    if "." in os.path.basename(path):
        path = os.path.dirname(path)

    if not path.endswith("/"):
        path += "/"

    return path


def is_valid_project_url(url, domain, base_path):
    parsed = urlparse(url)

    if parsed.netloc != domain:
        return False

    return parsed.path.startswith(base_path)


def is_alive(url):
    try:
        r = requests.head(url, timeout=4, allow_redirects=True)
        if r.status_code < 400:
            return True

        r = requests.get(url, timeout=4)
        return r.status_code < 400

    except Exception:
        return False


def get_links(url, domain, base_path):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        links = set()

        for a in soup.find_all("a", href=True):
            href = a["href"]
            full_url = urljoin(url, href)

            clean_url = normalize_url(full_url)

            if not is_valid_project_url(clean_url, domain, base_path):
                continue

            if not is_alive(clean_url):
                continue

            links.add(clean_url)

        return list(links)

    except Exception:
        return []


def build_tree(start_url, max_pages=30):
    parsed = urlparse(start_url)
    domain = parsed.netloc
    base_path = get_base_path(start_url)

    print(f"[INFO] Base path: {base_path}")

    root_url = normalize_url(start_url)
    root = Node(root_url)

    queue = deque([root])
    visited = set([root_url])

    while queue and len(visited) < max_pages:
        current_node = queue.popleft()

        links = get_links(current_node.url, domain, base_path)

        for link in links:
            norm_link = normalize_url(link)

            if norm_link not in visited:
                visited.add(norm_link)

                child = Node(norm_link)
                current_node.children.append(child)

                queue.append(child)

    return root


def print_tree(node, level=0):
    print("  " * level + f"- {node.url}")
    for child in node.children:
        print_tree(child, level + 1)
