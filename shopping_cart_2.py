import json
f= open("data_json.json",'r',encoding='utf8',errors='ignore')
data=f.read()

ind = data.index(':')
ind_=data.index(",")
ind2=data.index(":",ind+1)
ind2_=data.index(",",ind_+1)
ind3=data.index(":",ind2+1)
ind3_=data.index("}",ind3+1)

price=float(data[ind2+3:ind2_-1])
quantity=float(data[ind3+1:ind3_])

sum_=price*quantity

ind = data.index(':',ind3+1)
ind_=data.index(",",ind3_+2)
ind2=data.index(":",ind+1)
ind2_=data.index(",",ind_+1)
ind3=data.index(":",ind2+1)
ind3_=data.index("}",ind3+1)


price=float(data[ind2+3:ind2_-1])
quantity=float(data[ind3+1:ind3_])


sum_+=price*quantity


summa={}
summa['shipping']=0
summa['total']=sum_

f=open('data_json_w.json','w',encoding='utf8',errors='ignore')
json.dump(summa,f)