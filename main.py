import requests
from bs4 import BeautifulSoup

#dummy test for status code & html using requests
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers"
requestedURL = requests.get(url)
print(requestedURL.status_code)
print(requestedURL.text)

#dummy test for status code & html using beautifulsoup
soup = BeautifulSoup(requestedURL.text,"lxml")
print(soup)