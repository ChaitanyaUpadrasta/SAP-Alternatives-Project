import pandas as pd
import requests
from bs4 import BeautifulSoup
#C:\Users\Chaitanya Upadrasta\Downloads\pl.csv
master_df=pd.read_csv('D:\SEM-3\SAP-Project\pl_pdf.csv')
names=master_df['Product'].values.tolist()
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
F_df=df[df.Present!=False]
l=F_df.Product.values.tolist()
x=[]
for i in l:
    x.append(master_df[master_df.Product==i]['PDF_Link'].values[0])
F_df.to_csv('D:\SEM-3\SAP-Project\SAP_PDF_prod.csv')
