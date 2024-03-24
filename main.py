import requests
#its always good to use string value in a variable,then pass as argument.
url = "https://timesofindia.indiatimes.com/world"
r = requests.get(url)

print(type(r.text)) #<class 'str'>

print(type(r))  #<class 'requests.models.Response'>


def fetchSaveToFile(url, path):
    r=requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)
fetchSaveToFile(url, "data/ajio.html")