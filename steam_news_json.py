from typing import Dict

import requests

url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?"

params: dict[str, str] = {
    "appid": "440",
    "count": "3",
    "maxlength": "300",
    "format": "json"
}

r = requests.get(url, params=params).json()

news_for_users = r['appnews']['newsitems']

for news_for_user in news_for_users:
    title = news_for_user['title']
    url = news_for_user['url']

    print(title)
    print(url)
