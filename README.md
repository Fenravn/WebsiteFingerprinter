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

---

## 🧪 Tech Stack Fingerprinting Strategy
This tool inspects:

HTTP headers (Server, X-Powered-By)

<meta> tags (e.g., generator)

HTML comments or paths (coming soon)

Common URL patterns (coming soon)

---

## 🧠 Why This Exists
This project is part of my learning journey into cybersecurity and ethical hacking under the alias Fenravn. It serves as a base for deeper exploration into:

  Open Source Intelligence (OSINT)
  
  Reconnaissance automation
  
---

## 🧭 Future Plans
 Detect JS libraries (React, Vue, etc.)

 Scan for /wp-content/, /admin, etc.

 Output to file or JSON
 
 Build into a full CLI tool
 
 Add fingerprint database for more accuracy
 
---
## ⚖️ Disclaimer
This tool is intended for educational and ethical use only. Please do not scan websites without permission.
---
## 🐺 Fenravn
A quiet shadow in the binary forest. I study systems, signals, and silence. 
