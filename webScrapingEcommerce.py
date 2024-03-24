import requests
from bs4 import BeautifulSoup

url ="https://www.amazon.in/s?k=mobile&i=electronics&crid=2O7EYHVBBZ95H&sprefix=mobile%2Celectronics%2C237&ref=nb_sb_noss_1"
HEADERS= ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-language' : 'en-US, en;q=0.5'})


webpage = requests.get(url, headers=HEADERS)
print(type(webpage.content))
soup= BeautifulSoup(webpage.content, 'html-parser')
soup

# proxies = {
#   "https": "scraperapi.country_code=us.device_type=mobile.session_number=50:05f7ecf76710c9b2bf686698b95fac0a@proxy-server.scraperapi.com:8001"
# }
# r = requests.get('https://www.amazon.in/s?k=mobile&i=electronics&crid=2O7EYHVBBZ95H&sprefix=mobile%2Celectronics%2C237&ref=nb_sb_noss_1', proxies=proxies, verify=False)
# print(r.text)