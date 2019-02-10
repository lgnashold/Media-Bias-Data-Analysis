import urllib.request
from bs4 import BeautifulSoup
import html5lib
import re



x = urllib.request.urlopen("https://www.allsides.com/news/2017-03-30-0658/california%E2%80%99s-moral-atrocity")
html_doc = x.read().decode('utf-8')

soup_int = BeautifulSoup(html_doc, 'html.parser')
    
print(soup_int.find(id="source-bias-info-block").find('img').get("alt"))

link = soup_int.find("iframe").get("src")

article = urllib.request.Request(link,headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',} )

article = urllib.request.urlopen(article).read().decode("utf-8")


soup_art = BeautifulSoup(article, "html5lib")

#print(len(soup_art.find_all("article")))

if len(soup_art.find_all("article")) == 1:
   print("FOUND ARTICLE TAG")
   soup_art = soup_art.find("article")

# kill all script and style elements
for script in soup_art(["script", "style"]):
    script.decompose()    # rip it out

#kill all things classes as "comment"

for comment in soup_art.find_all(class_=re.compile("comment")):
   comment.decompose()

for comment in soup_art.find_all(id=re.compile("comment")):
   comment.decompose()

#CURRENT METHOD:  Only get paragraphs in text.

text = ""

for p in soup_art.find_all("p"):
   text += p.get_text()


#OTHER METHOD TRIES TO GET ALL TEXT, MORE CLUTTERt
# text = soup_art.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

