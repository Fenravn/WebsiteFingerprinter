# 🕵️‍♂️ Website Fingerprinter

A simple Python tool that analyzes a website and identifies clues about its tech stack — including HTTP headers, CMS indicators, and HTML metadata.

Created by **Fenravn** as a first step into ethical hacking and reconnaissance tooling.

---

## 🚀 Features

- 📡 Fetches and displays HTTP headers
- 🔍 Extracts meta tags (like CMS info)
- 🧠 Helps you identify tech stacks (PHP, WordPress, Nginx, etc.)
- 🛠️ Beginner-friendly and extendable

---

## 📦 Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install them with:

```bash```
pip install requests beautifulsoup4

---

## How To Use!
python fingerprint.py
Then enter a full website URL, like:
https://example.com

---

## Sample Output
Enter a URL (with https://): https://wordpress.com

=== HTTP HEADERS ===
Server: nginx
X-Powered-By: PHP/7.4.3

=== META TAGS ===
Generator: WordPress 5.9


