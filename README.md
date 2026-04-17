# Docs Crawler

A Python tool that crawls documentation websites, downloads HTML pages and assets, and converts everything into a single Markdown file.

#### Usage
```sh
python src/main.py input.txt
```

input.txt should contain a list of documentation URLs.

#### Output

For each URL, the tool generates:

- downloaded HTML (html/)
- assets (assets/)
- final docs.md file
