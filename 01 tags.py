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

# print(soup.a)   #<a href="https://google.com">Google</a>
# print(soup.p)

# print(soup.find(id = "link3"))  #<a href="https://apublicn" id="link3">public</a>
# #find all kinks by href
# l = []
# for link in soup.find_all("a"):
#     l.append(link.get("href"))
#     print(link.get_text())    # https://google.com
# print(l)

# s = soup.find(id = "link3")
# print(s.get("href"))
# print(s.get_text())  #public

#SElecting element using selectors i.e   # & .
# print(soup.select("div.italic")) #in case of multiple div ,it will output in List

# #to get a span whose id is italic
# print(soup.select("span#italic"))
# #to get list of all classes for span
# print(soup.span.get("class"))
# print(soup.find(id="italic")) #to find tags with whose id is italic
# print(soup.find(class_="italic")) #class is reserved  so use class_


##TO find all the  children tags of a parent tag
# for child in soup.find(class_="container").children:
#     print(child)  #children of div class container

#To find parent of any tag
# for parent in soup.find(class_="box").parents:
#     print(parent)  #first it will print parent of box i.e container. Then body part as parent of container and then the total html tag as parent of webpage

cont = soup.find(class_="container")
print(cont)
#modifying the div to span
cont.name="span"
print(cont)
cont["class"]="myclass class1"
print(cont)






