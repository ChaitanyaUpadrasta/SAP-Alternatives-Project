import pandas as pd
import requests
from bs4 import BeautifulSoup
#C:\Users\Chaitanya Upadrasta\Downloads\pl.csv
master_df = pd.read_csv(r'pln_pdf.csv')
master_df.Product

names=master_df['Product'].to_list()
URL="https://www.trustradius.com/vendors/sap"
r=requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
a=[]
b=[]
df=pd.DataFrame()
x=soup.find_all('a',attrs = {'class':"ProductGridProduct_product__2iNPt"})
for i in x:
    y=i.find('h3',attrs={'class':"ProductGridProduct_name__W3FLG h4"})
    a.append(y.text)
    b.append(y.text in names)
    
df['Product']=a
df['Present']=b
df[df.Present!=False].to_csv('Our_Target_Products_nopdf.csv')