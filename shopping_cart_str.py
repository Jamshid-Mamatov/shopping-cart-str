from pprint import pprint
import json

f=open("shopping_cart.json",'r',encoding='utf8',errors='ignore')
data=f.read().split(',')
# print(data)
product=[]
for item in data:
    ind=item.index(':')
    product.append(item[ind+1:])
for i, j in enumerate(product):
    product[i] = j.replace(' \n}','')
for i, j in enumerate(product):
    product[i] = j.replace('"','')   
for i, j in enumerate(product):
    product[i] = j.replace('$','') 
print(product)
