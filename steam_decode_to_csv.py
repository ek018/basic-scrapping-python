from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

url = 'https://store.steampowered.com/explore/new/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

new_releases = soup.findAll('a', attrs={'class': 'tab_item'})
file = open('steam_data_new_release.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])

for new_release in new_releases:
    if new_release.find('div', attrs={'class': 'tab_item_name'}) is not None:
        title = new_release.find('div', attrs={'class': 'tab_item_name'}).text
    else:
        title = ''
    if new_release.find('div', attrs={'class': 'discount_final_price'}) is not None:
        price = new_release.find('div', attrs={'class': 'discount_final_price'}).text
    else:
        price = ''
    if new_release.find('div', attrs={'class': 'tab_item_top_tags'}) is not None:
        tags = new_release.find('div', attrs={'class': 'tab_item_top_tags'}).text
    else:
        tags = ''
    file = open('steam_data_new_release.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tags])
    file.close()
