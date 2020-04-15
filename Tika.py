from tika import parser
import pandas as pd
import requests
from tika import parser
import re

df=pd.read_csv(r'D:\SEM-3\SAP-Project\SAP_PDF_prod.csv')
urls=df['PDF_Link'].values.tolist()
a=[]
for i in range (len(urls)):
    
    response = requests.get(urls[i])
    response
    with open('D:\SEM-3\SAP-Project\metadata%i.pdf' %i, 'wb') as f:
         f.write(response.content)  
a=[]

for i in range (len(urls)):

    raw = parser.from_file('D:\SEM-3\SAP-Project\metadata%i.pdf' %i)
    data = raw['content']

    data = data.replace("\u2009", " ")
    data = data.replace("\u00ae", " ") # registered
    data = data.replace("\u2022", ".") #bullet
    data = data.replace("\u00a9", " ") # copyright
    data = data.replace("\u201c", '"') #left double quote
    data = data.replace("\u201d", '"') #right double quote
    data = data.replace("\u2019", "'") #single quote
    data = data.replace("- ", "")
    data = data.replace("  ", " ")
    data = data.replace("  ", " ")
    data = data.replace('\n','')
    data = data.replace('\t','')
    URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)(?:(?:\/[^\s/]))*', '', data) # Remove http urls
    a.append(URLless_string)
    
df['description']=a
df.to_csv('D:\SEM-3\SAP-Project\SAP_data.csv')