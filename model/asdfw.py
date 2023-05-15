from bs4 import BeautifulSoup
import requests 
import time
import re
from urllib.parse import urlparse
import json 
url = "https://youtube.com"
urlparse = urlparse(url)
domain = urlparse.netloc
print(domain)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
data = 'https://www.similarweb.com/website/'+domain

response = requests.get(data, headers=header)
time.sleep(5)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
div = soup.find('p', {"class" : "wa-rank-list__value"})
text = div
print(text)