import requests, re
from bs4 import BeautifulSoup
import pandas as pd


url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
print(url.status_code)

#dummy test for status code & html using beautifulsoup
soup = BeautifulSoup(url.text,"lxml")           #Init bs

#TAGS
tagDiv = soup.div                                  
tagHeader = soup.header
tagDivParagraph = soup.div.p            #<p> p tag included like this </p>
tagDivParagraphString = soup.div.p.string   #HTML tag not included
tagLongExample = soup.header.div.a.button.span  #go to the innermost tag

#ATTRIBUTES
print(tagDiv.attrs)                                
print(tagHeader.attrs)
print(tagHeader.attrs["class"])

#NAVIGABLE STRINGS
print(tagDivParagraph)
print(tagDivParagraphString)    #don't have to use .string if defined in the tag
print(tagLongExample.string)    #adding .string will remove HTML tags <></>

#FIND
print(soup.find("p",{"class":"description"})) #limited to the first div tag that it finds

#FINDALL
prices = soup.find_all("h4",class_ = "pull-right price")
desc = soup.find_all("p",class_ = "description")
print(len(desc))
for i in desc:
    print(i.text)
print("Desc[2] = ",desc[2])

#REGULAR EXPRESSIONS
data = soup.find_all(string=re.compile("Galaxy"))
print(data)
print(len(data))

#PANDAS
names = soup.find_all("a", class_ = "title")
print("\nNames: ",names)

product_name = []
product_desc=[]

for i in names:
    product_name.append(i.text)
print("\nNames in a list: ",product_name)

for i in desc:
    product_desc.append(i.text)
print("\nDescriptions in a list: ",product_desc)


df = pd.DataFrame({"Product Name":product_name,"Descriptions":product_desc})
print(df)
df.to_csv("product_details.csv")    #send to CSV
df.to_excel("product_details_excel.xlsx", engine='openpyxl') #send to excel