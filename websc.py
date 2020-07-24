import requests
from bs4 import BeautifulSoup
#import os,sys
url='https://robinhood.com/collections/technology'
r=requests.get(url)
html=r.content

soup=BeautifulSoup(html,'html.parser') 

#sys.exit()
all_links=soup.find_all('a')

for link in all_links:
     if "http" in link.get("href"):
         print ("<a href='%s'>%s</a>" %(link.get("href"), link.text))
         
data=soup.find_all("span",{"class":"css-13cafbm"})

for item in data:
    print (item.contents[0].find_all("div",{"class":"kg7H31Ap4MW-dg1bFNOGP"})[0].text)
    print (item.contents[0].find_all("div",{"class":"kg7H31Ap4MW-dg1bFNOGP"})[0].text)
    print (item.contents[0].find_all("div",{"class":"_1OFbcHb21BVF-HUMyM5v7i"})[0].text)

#saving the file
file = open("data1.txt", "w") 
file.write(str(html))
file.close()
