
import json
f1=open("items.json","r")
f2=open("country-val.json","w")
f3=open("name.json","w")
js=json.load(f1)

txt1=js["variables"]
txt2=js["entityKey"]
num=txt1.keys()[0]
print txt1[num].keys()
print txt1[num]['name']
dataset_name=txt1[num]['name']
entities_data=txt1[num]["entities"]
years_data=txt1[num]["years"]
values_data=txt1[num]["values"]


#every code in entitles represent the contry_code which is defined in txt2,then is the years and values,easy to understand
items={}
for i in range(len(years_data)):
    index = entities_data[i]
    items[txt2[str(index)]["name"]]=values_data[i]


string9=json.dumps(items)
f3.write(dataset_name)
"""
string1=(json.dumps(txt1)+"\n")
string2=(json.dumps(txt2)+"\n")
string3=(json.dumps(entities_data)+"\n")
string4=(json.dumps(years_data)+"\n")
string5=(json.dumps(values_data)+"\n")
description   NULL
entities    ****
created_at  time
years     *****
source   doc
values  *****
dataset_name  overty headcount at $1.90 a day
id          183
unit   %
name          Poverty headcount at $1.90 a day (2011 PPP)
"""



f2.write(string9)
f1.close()
f2.close()
f3.close()
