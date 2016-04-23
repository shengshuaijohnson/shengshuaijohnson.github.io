import getval
import json
import string
file=open("Border data.json","r")
file0=open("country-val.json","r")

file3=open("name.json","r")
border=json.load(file)
val=json.load(file0)

def findmax(data):  
    max=0
    for i in data:
        if float(data[i])>float(max):
           max=float(data[i])
    return max
def findmin(data):  
    min=9999999999
    for i in data:
        if float(data[i])<float(min):
           min=float(data[i])
    return min
min=float(findmin(val))
max=float(findmax(val))
#max-=min
print max
val2=val
for i in val2:
    val2[i]=float(val2[i])
    #val2[i]-=min
    val2[i]=val2[i]/max



ultimat=[]
for name in val2:
    for tmp in border:
        if name==tmp:
            flag=0
            the_val=val2[name]  #the_val is the val
            for i in border[name]:
                ultimat.append(i)
                flag+=1
                if flag==2:
                    ultimat.append(0.25*the_val)
                    flag=0
style=[]
style.append("1990")
style.append(ultimat)
ultimat=[]
ultimat.append(style)
dataset_name=file3.read()

#dataset_name=dataset_name[0:-1]
print dataset_name
dataset_name="data/"+dataset_name+".json"

file2=open(dataset_name,"w")
file2.write(json.dumps(ultimat))

file.close()
file0.close()
file2.close()
file3.close()
