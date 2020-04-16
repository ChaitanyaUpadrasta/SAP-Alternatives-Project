import pandas as pd
import requests
from bs4 import BeautifulSoup
#C:\Users\Chaitanya Upadrasta\Downloads\pl.csv

total_df=pd.read_csv('D:\SEM-3\SAP_Project\pl.csv')
total_df
names=total_df['Product'].values.tolist()
len(names)
URL="https://www.trustradius.com/vendors/sap"
r=requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
x=soup.find_all('a',attrs = {'class':"ProductGridProduct_product__2iNPt"})
links=[]
a=[]
b=[]
df=pd.DataFrame()
for i in x:
    
    y=i.find('h3',attrs={'class':"ProductGridProduct_name__W3FLG h4"})
    if y.text in names:
        a.append(y.text)
        links.append("https://www.trustradius.com"+i.get('href'))
df['Product']=a
df['Reviews']=links
u=df.Reviews.values.tolist()
Alternatives=[]
Product_link=[]
for i in u:
    u=i[:i.rfind('/')]
    Alternatives.append(u+'/competitors')
    Product_link.append(u+'/reviews#1')
df['Alternatives']=Alternatives
df['Product_link']=Product_link
Alter_of=df.Product.values.tolist()
Alter_df=pd.DataFrame()
Alternative_for=[]
Product=[]
Link=[]
for i in range(len(Alternatives)):
    req=requests.get(Alternatives[i])
    soup = BeautifulSoup(req.content, 'html5lib')
    x=soup.find('section')
    y=x.find_all('a')

    for j in y[0:4]:
        Link.append('https://www.trustradius.com'+j.get('href'))
        Product.append((j.find('h3').text))
        Alternative_for.append(Alter_of[i])
Alter_df['Product']=Product
Alter_df['Link']=Link
Alter_df['Alternative_for']=Alternative_for
Alter_df.to_csv('D:\SEM-3\SAP_Project\Alternatives.csv')