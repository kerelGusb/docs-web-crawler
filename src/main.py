import argparse
from pathlib import Path

from link_tree import LinkTree
from docs_download import DocsDownload, Downloader
from md_builder import MarkdownBuilder


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent
    output_dir = base_dir / "output"

    try:
        with open(args.filepath, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: file not found")
        return

    if not urls:
        print("File is empty")
        return

    downloader = Downloader()

    success = 0
    failed = 0

    for url in urls:
        print(f"\n=== PROCESSING: {url} ===")

        try:
            tree = LinkTree(url, max_pages=1000, debug=args.debug)

            docs = DocsDownload(
                link_tree=tree,
                downloader=downloader,
                output_dir=output_dir
            )
            docs.run()

            project_dir = Path(docs.project_dir)

            builder = MarkdownBuilder(
                project_dir=str(project_dir),
                output_file=str(project_dir / "docs.md")
            )

            builder.build(tree.root)

            success += 1
            print(f"[OK] finished: {url}")

        except Exception as e:
            failed += 1
            print(f"[ERROR] failed: {url}")
            print(f"[ERROR] reason: {e}")

    print("\n=== SUMMARY ===")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print("DONE")


if __name__ == "__main__":
    main()