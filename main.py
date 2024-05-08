import requests
from bs4 import BeautifulSoup

url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers")
print(url.status_code)

#dummy test for status code & html using beautifulsoup
soup = BeautifulSoup(url.text,"lxml")           #Init bs

tagDiv = soup.div                                  #set tags
tagHeader = soup.header

print(tagDiv.attrs)                                #print attributes
print(tagHeader.attrs)
print(tagHeader.attrs["class"])