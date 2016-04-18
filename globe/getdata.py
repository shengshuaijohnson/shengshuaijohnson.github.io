import json
import string
file=open("Border data.json","r")
file0=open("country-val.json","r")
file2=open("population909500.json","w")

border=json.load(file)
val=json.load(file0)

def findmax(data):  
    max=0 
    for i in data:
        if data[i]>max:
           max=data[i]
    return max
max=float(findmax(val))
val2=val
for i in val2:
    val2[i]=float(val2[i])/max



ultimat=[]
for name in val2:
    for tmp in border:
        if name==tmp:
            flag=0
            the_val=val2[name]
            for i in border[name]:
                ultimat.append(i)
                flag+=1
                if flag==2:
                    ultimat.append(0.10*the_val)
                    flag=0
style=[]
style.append("1990")
style.append(ultimat)
ultimat=[]
ultimat.append(style)

file2.write(json.dumps(ultimat))
"""

for i in range(len(con)):
    if (con[i]!=''):
        items.append(string.atof(con[i]))
        flag+=1
        if(flag==2):
            flag=0
            items.append(0.3)
print items




pos=0
while(pos<len(items)):
    (items[pos],items[pos+1])=(items[pos+1],items[pos])
    pos+=3


"""
file.close()
file0.close()
file2.close()
