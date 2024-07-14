strings=input("enter the string= ")
v=strings.lower()
v=list(v)
length=len(v)
for i in range(0,length):
    if v[i]=="a" or v[i]=="e" or v[i]=="i" or v[i]=="o" or v[i]=="u":
        v.pop(i)
        v.insert(i,"")
for i in v:
   print(i,end="")