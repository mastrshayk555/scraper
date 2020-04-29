#from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup

import pandas
import requests
from bs4 import BeautifulSoup

#getting the webpage
webpage = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38')

#list of all products on page
content = webpage.content

#parsing the content
result = BeautifulSoup(content, 'html.parser')
  
#html parsing or organizing the page
#page_soup = soup(page_html, "html.parser")

#grabs each product
containers = result.find_all("div", class_="item-container")

#print(len(containers))
#print(containers[0])

#for container in containers:
#	brand_1 = container.find(

for container in containers:
	br_contain = container.find("div", class_="item-info")
brand = container.find("img", "title").str

#	title_container = container.find("a", {"class": "item-title"})
	#product_name = title_container[0].text

print(brand)



