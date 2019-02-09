import urllib.request
from bs4 import BeautifulSoup
import re

for i in range(0,10):

    x = urllib.request.urlopen("https://www.allsides.com/topics/abortion?page="+str(i))
    html_doc = x.read().decode('utf-8')
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    for link in soup.find_all("div", class_ = re.compile("news\-title")):
        print(link.find('a').get("href"));
