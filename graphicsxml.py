import pandas
import requests
from bs4 import BeautifulSoup

#getting the webpage
webpage = requests.get('https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38')

#list of all products on page
content = webpage.content

#parsing the content
soup = BeautifulSoup(content, 'lxml')
  
#html parsing or organizing the page
#page_soup = soup(page_html, "html.parser")

#grabs each product
containers = soup.find_all("div", class_="item-container")

##//Making sure I can locate the first container
#print(containers)

#container = containers[0]
#print(container) #Yes this locates the first container/card on the page
##//End check


brand = []
discription = []
price = []
#shipping = []


#for container in containers:
#	cont_brand = container.find_all("div",{"class":"item-info"})
#brand = cont_brand[0].div.a.img["alt"]

#print(brand)



#data = (list(zip(brand)))

#print(data)
#d = pandas.DataFrame(data, columns = [brand])
#print(d)