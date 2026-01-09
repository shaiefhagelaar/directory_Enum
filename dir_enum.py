import requests
import time

dirs = ["admin", "upload", "uploads", "files", "api", "images", "css", "js", "assets"]
target = "http://example.com"

for d in dirs:
    try:
        r = requests.get(f"{target}/{d}/", timeout=5)
        print(f"Checking /{d}: {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking /{d}: {e}")
    time.sleep(0.5)
