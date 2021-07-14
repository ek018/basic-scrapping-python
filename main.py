import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def get_top_sellers():
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
        print('Price :', top_seller.find('div', attrs={'class': 'search_price'}).text)

    return render_template('grid_template.html', top_sellers=top_sellers)


if __name__ == '__main__':
    app.run(debug=True)
