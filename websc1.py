#scraping the stock price of MICROSOFT

import requests
from bs4 import BeautifulSoup
#import os,sys
def websc():
    
    r=requests.get('https://finance.yahoo.com/quote/MSFT/')
    html=r.content

    soup=BeautifulSoup(html,'html.parser') 
    all_data1=soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('span').text
    
    return all_data1

while True:
    print('Current Price of Microsoft is ',websc())





#saving the file
file = open("microsoft.txt", "w") 
file.write(str(html))
file.close()



