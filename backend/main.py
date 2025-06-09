import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to fetch page. Status code: {response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    posts = []
    for post_div in soup.find_all("div", class_="x1i10hfl"):  # You may need to update this class
        try:
            text = post_div.get_text(strip=True)
            posts.append({
                "text": text[:300],  # First 300 chars
            })
        except:
            continue

    return posts[:10]
