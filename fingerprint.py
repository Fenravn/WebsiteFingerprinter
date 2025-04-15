import requests
from bs4 import BeautifulSoup

def get_headers(url):
    try:
        response = requests.get(url, timeout=10)
        print("=== HTTP HEADERS ===")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestsException as e:
        print(f"Error fetching headers: {e}")

def get_meta_tags(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("\n=== META TAGS ===")
        for meta in soup.find_all('meta'):
            if meta.get('name') == 'generator':
                print(f"Generator: {meta.get('content')}")
    except requests.RequestException as e:
        print(f"Error fetching HTML: {e}")

if __name__ == "__main__":
    target_url = input("Enter a URL (with https://): ")
    get_headers(target_url)
    get_meta_tags(target_url)
