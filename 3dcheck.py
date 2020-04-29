import pandas
import requests
from bs4 import BeautifulSoup

#getting the webpage
webpage = requests.get("https://shop3duniverse.com/collections/1-75mm-filaments")

#list of all products on page
content = webpage.content

#parsing the content
result = BeautifulSoup(content, 'html.parser')

#ID the poducts on the page
products = result.find_all("div", {"class": "product-tile"})

#product = products[0]
#print(product)

for item in products:
    item_vendor = item.find("div", {"class": "vendor"})
    vendor = item_vendor[0].str

print(len(vendor))
#print(item_vendor)





#create a list of each desired piece of info
#brand = []
#material = []
#price = []
#link= []

#iterating over the list of products and extracting necessary info
#get rid of whitespace with .string.strip()
#for item in products:
#    brand.append(item.find("div", {"class": "vendor"}).string)
#    material.append(item.find("span", {"style": "front-weight: 400;"}))
#    price.append(item.find("div", {"class": "price"}).text.strip())
#    link.append("https://www.shop3duniverse.com" + item.a['href'])

