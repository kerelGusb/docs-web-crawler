import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import os

BAD_EXTENSIONS = {
    ".xml", ".json", ".txt", ".csv", ".md", ".yaml", ".yml"
}

class Node:
    def __init__(self, url):
        self.url = url
        self.children = []


def normalize_url(url):
    parsed = urlparse(url)

    path = parsed.path

    if path.endswith("/index.html"):
        path = path[:-10]


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

def is_html_like(url):
    path = urlparse(url).path.lower()
    return not any(path.endswith(ext) for ext in BAD_EXTENSIONS)


def get_links(url, domain, base_path, session):
    try:
        response = session.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        links = set()

        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            clean_url = normalize_url(full_url)

            if not is_valid_project_url(clean_url, domain, base_path):
                continue
            
            if not is_html_like(clean_url):
                continue

            links.add(clean_url)

        return list(links)

    except Exception:
        return []


def build_tree(start_url, max_pages=300, debug=False):
    parsed = urlparse(start_url)
    domain = parsed.netloc
    base_path = get_base_path(start_url)
    session = requests.Session()

    print(f"Base path: {base_path}")

    root_url = normalize_url(start_url)
    root = Node(root_url)

    queue = deque([root])
    visited = set([root_url])

    while queue and len(visited) < max_pages:
        current_node = queue.popleft()

        if debug:
            print(f"[DEBUG] solving URLs from {current_node.url}")

        links = get_links(current_node.url, domain, base_path, session)

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
        
if __name__ == "__main__":
    START_URL = "https://commons.apache.org/proper/commons-vfs/project-info.html"

    tree = build_tree(START_URL)

    print("\n=== URL TREE ===\n")
    print_tree(tree)
