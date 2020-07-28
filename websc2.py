import requests
from bs4 import BeautifulSoup

def stock():
    url='https://robinhood.com/collections/technology'
    req=requests.get(url)
    html=req.content
    soup=BeautifulSoup(html,'html.parser')
    
    stock2=soup.find_all('a',{'class':'rh-hyperlink qD5a4psv-CV7GnWdHxLvn AaXTyP3x99eRIDW0ExfYP'})[2].text
    
    return stock2



while True:
    print('The Stock price of Apple at present is ', stock())
    
#saving the file
file = open("apple.txt", "w") 
file.write(str(html))
file.close()


