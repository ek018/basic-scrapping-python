import requests
from bs4 import BeautifulSoup


headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36 '
    }
url = "https://store.steampowered.com/search/?filter=topsellers"

r = requests.get(url, headers=headers)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
top_sellers = soup.findAll('a', attrs={'class': 'search_result_row ds_collapse_flag'})
# print(top_sellers)
for top_seller in top_sellers:
    print('Title :', top_seller.find('span', attrs={'class': 'title'}).text)
    print('Image :', top_seller.find('div', attrs={'class': 'search_capsule'}).find('img'))
    # print('Price :', top_seller.find('div', attrs={'class': 'search_price'}).text)
    # print('Price :', top_seller.find('div', attrs={'class': 'search_price'}).find('br').next_element)
    # after_discount = top_seller.find('div', attrs={'class': 'search_price'}).find('br').next_element
    before_discount = top_seller.find('div', attrs={'class': 'search_price'}).find('strike').text if top_seller.find('div', attrs={'class': 'search_price'}).find('strike') is not None else top_seller.find('div', attrs={'class': 'search_price'}).text
    # test: object = after_discount if after_discount else None
    print('test:',before_discount)
    
    # kurang tampilin harga yg None di GTA