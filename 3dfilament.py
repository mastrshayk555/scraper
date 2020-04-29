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

#create a list of each desired piece of info
brand = []
#material = []
price = []
link = []

#iterating over the list of products and extracting necessary info
#get rid of whitespace with .string.strip()
for item in products:
    brand.append(item.find("div", {"class": "vendor"}).string)
    #material.append(item.find("span", {"style": "front-weight: 400;"}))
    price.append(item.get_text("div", {"class": "price"}).strip())
    link.append("https://www.shop3duniverse.com" + item.a['href'])

#removed material
data = list(zip(brand, price, link))

#creating the pandas dataframe
# removed, 'Material' after brand
d = pandas.DataFrame(data, columns = ['Brand', 'Price', 'Link'])

#Writing the dataframe to an excel file
try:
    d.to_csv("~//Desktop//scraper//shop3duniverse1_75mm.ods")

except:
    print("\nShit's on FIRE. Stop and check your code dumbass.")

else:
    print("\nYep all done.")

finally:
    print("\nApplication Complete. Terminate!")

#End of Program    



