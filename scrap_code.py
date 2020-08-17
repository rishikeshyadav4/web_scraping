#scraping the mask price at amazon
import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
r=requests.get('https://www.amazon.in/s?k=Reusable+Washable+Face+Mask+with+Breathing+Valve&ref=nb_sb_noss')
html=r.content

soup=BeautifulSoup(html,'html.parser') 
all_data1=soup.find_all('div',{'class':'s-main-slot s-result-list s-search-results sg-row'})
    
index = 0
file={}
conn=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='rANJUYADAv@123',
            database='my_data'
            )
curr=conn.cursor()

def websc():
    
    for data in all_data1:
           
        #global name
        #global price
        name = data.find('span',{'class':'a-size-base a-color-base a-text-normal'})[0].text
        price = data.find('span',{'class':'a-price-whole'})[0].text
        
        #print('Name',name,'\nPrice',price)
        index += 1
        file[index]=[name]
        file[index]=[price]
file_df=pd.DataFrame.from_dict(file, orient='index', columns=['Name','Index'])
print(file_df)  
        
        
def create_table():
    
    curr.execute("""DROP TABLE IF EXISTS data_table """)
    conn.commit()
    
    for items in file:
        
        
        t_name=items['Name']
        t_price=items['Index']
        
        add_item = ("INSERT INTO data_table "
                    "(name, price) "
                    "VALUES (%s, %s)")
        data_item = (t_name, t_price)
        cursor.execute(add_item, data_item)
        conn.commit()
        
create_table()
websc()


  


