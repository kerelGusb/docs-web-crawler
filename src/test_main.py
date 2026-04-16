from link_tree import LinkTree
from docs_download import Downloader, DocsDownload

def main():
    url = "https://freemarker.apache.org/docs/index.html"

    tree = LinkTree(url, max_pages=20)
    downloader = Downloader()

    docs = DocsDownload(tree, downloader, output_dir="test_output")
    docs.run()

    print("DONE")


if __name__ == "__main__":
    main()