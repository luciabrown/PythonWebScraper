import requests
from bs4 import BeautifulSoup

url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers")
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