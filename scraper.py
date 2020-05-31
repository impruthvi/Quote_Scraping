# http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
base_url = "http://quotes.toscrape.com"
url = "/page/1"
all_quotes = []

while url:


    res = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}")
    soup = BeautifulSoup(res.text,"html.parser")
    quotes = soup.find_all(class_ = "quote")
    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_ = "text").get_text(),
            "author":quote.find(class_ = "author").get_text(),
            "bio-link":quote.find("a")["href"]
        })
    next_btn = soup.find(class_ = "next")
    url = next_btn.find("a")["href"] if next_btn else None

print(all_quotes)