import requests
from bs4 import BeautifulSoup

counts = input()
pos = input()

def web_crawl(url):
    lst = list()
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a'):
        title = link.get('href', None)
        lst.append(title)
    new_url = send_to_next(lst)
    for i in range(counts-1):
        web_crawl(new_url)

def send_to_next(lst):
    url = lst[pos]
    return url

web_crawl('http://python-data.dr-chuck.net/known_by_Fikret.html')