import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.114 Safari/537.36 '
}

url = "https://store.steampowered.com/"
r = requests.get(url, headers=headers)
print(r)
soup = BeautifulSoup(r.text, "html.parser")
carousel_items_steam = soup.findAll('div',attrs={'class': 'carousel_items'})

for data in carousel_items_steam:
    print(data)
