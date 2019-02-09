import urllib.request
from bs4 import BeautifulSoup

x = urllib.request.urlopen("https://www.allsides.com/topics-issues")
html_doc = x.read().decode('utf-8')

soup = BeautifulSoup(html_doc, 'html.parser')

for link in filter(None, soup.find_all('a')):
    if str(link.get('href')).startswith("/topics/"):
       print("https://www.allsides.com" + str(link.get('href')))
