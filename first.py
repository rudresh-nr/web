import random
import urllib

def download_we_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) +".jpg"
    urllib.urlretrieve(url,full_name)

download_we_image("http://cdn.wealthygorilla.com/wp-content/uploads/2015/03/Top-Blogs-for-Entrepreneurs-in-20151.jpg")
