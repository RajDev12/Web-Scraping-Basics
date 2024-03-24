import requests

# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "https://10.10.1.10:1080",
# }
# proxy = {
#   "https": ""
# }

import requests
proxies = {
  "http": "scraperapi.retry_404=true.session_number=50:05f7ecf76710c9b2bf686698b95fac0a@proxy-server.scraperapi.com:8001",
  "https": "scraperapi.retry_404=true.session_number=50:05f7ecf76710c9b2bf686698b95fac0a@proxy-server.scraperapi.com:8001"
}
r = requests.get('https://timesofindia.indiatimes.com/city/Mumbai', proxies=proxies, verify=False)
print(r.text)

# proxies={
#         "http": "scraperapi.country_code=us.device_type=desktop.session_number=500:05f7ecf76710c9b2bf686698b95fac0a@proxy-server.scraperapi.com:8001",
#         "https" : "scraperapi.country_code=us.device_type=desktop.session_number=500:05f7ecf76710c9b2bf686698b95fac0a@proxy-server.scraperapi.com:8001"
# }
# #using ipify api to find ip
# r = requests.get("https://api64.ipify.org?format=json", proxies=proxies, verify=True)
# print(r.text)     #{"ip":"103.16.147.94"}