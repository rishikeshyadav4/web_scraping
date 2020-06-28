#web scraping daraz.com.np

import requests
from bs4 import BeautifulSoup
url='https://www.daraz.com.np/catalog/?q=guitar&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.287d2d2bR3WCJo'
r=requests.get(url)   # r is a variable
html=r.content    # to see the html content

soup=BeautifulSoup(html) #accessible to beautiful soup
soup.prettify()

all_links=soup.find_all("a")

for link in all_links:
     if "http" in link.get("href"):
         print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
         
data=soup.findall("div",{"class":"c5TXIP"})

for item in g_data:
    print item.contents[0].find_all("div",{"class":"c3gUW0"})[0].text
    print item.contents[0].find_all("span",{"class":"c1hkC1"})[0].text
