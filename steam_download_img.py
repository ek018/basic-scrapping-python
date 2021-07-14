import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

url = 'https://store.steampowered.com/genre/Free%20to%20Play/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
free_games = soup.find('div', attrs={'id': 'NewReleasesRows'})
new_release_contents = free_games.findAll('a', attrs={'class': 'tab_item'})

for new_release_content in new_release_contents:
    imageUrl = new_release_content.find('img', attrs={'class': 'tab_item_cap_img'})['src']
    title = new_release_content.find('div', attrs={'class': 'tab_item_name'}).text
    response = requests.get(imageUrl, headers=headers, stream=True)
    fileName = imageUrl.split("/")[-1].split("?")[0]
    ext = fileName[-4:]
    if response.ok:
        with open('images/' + re.sub(r'(?u)[^_\w.]','_', title) + ext, 'wb') as a:
            a.write(response.content)