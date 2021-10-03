from bs4 import BeautifulSoup #import BeautifulSoup

import requests #import requests

#scrape all the markup text using BeautifulSoup from https://www.nytimes.com/crosswords/game/mini
source = requests.get('https://www.nytimes.com/crosswords/game/mini.html').text 

#The App uses lxml library for easy handling of HTML data
soup = BeautifulSoup(source, 'lxml') 

#print(soup)
#print out the scrapped html data in a formatted order using prettify() Library
print(soup.prettify())