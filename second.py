import requests
from bs4 import BeautifulSoup

def trade_spider():
    lst = list()
    url = 'http://python-data.dr-chuck.net/comments_324048.html'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for num in soup.findAll('span', {'class': 'comments'}):
        title = num.string
        lst.append(int(title))

    summ(lst)

def summ(lst):
    total = 0
    for num in lst:
        total +=  num
    print(total)


trade_spider()

