import requests
from bs4 import BeautifulSoup

##step 1= open the index.html in read file mode
with open("index.html", "r") as f:
    html_doc = f.read()
##step 2= pass the html doc to to make a soup object
soup = BeautifulSoup(html_doc, 'html.parser' )
# print(type(soup))  #<class 'bs4.BeautifulSoup'> a soup object
# print(soup.prettify())
# print(soup.title)
# ## Name of the title of webpage
# print(soup.title.string, type(soup.title.string)) #'bs4.element.NavigableString 
# print(soup.title.parent.name)  #head
# #To show the 1st occurence of the tag
# print(soup.div)
## find_all ouputs list of all tags
# print(soup.find_all("div"))
# print(soup.find_all("div")[0])   #For teh 1st the elelment

print(soup.a)   #<a href="https://google.com">Google</a>
print(soup.p)

print(soup.find(id = "link3"))  #<a href="https://apublicn" id="link3">public</a>
#find all kinks by href
l = []
for link in soup.find_all("a"):
    l.append(link.get("href"))
    print(link.get_text())    # https://google.com
print(l)

s = soup.find(id = "link3")
print(s.get("href"))
print(s.get_text())  #public
print(soup.select("div.italic")) #in case of multiple div ,it will output in List

print(soup.select("span#italic"))
print(soup.span.get("class"))







