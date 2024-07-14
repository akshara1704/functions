l1=[3,55,76,8123,0,777,109,-1,44]
compMax=l1[0]
max1=0
mini1=0
compMin=l1[0]
for i in range(0,len(l1)):
    if l1[i]>compMax:
        max1=l1[i]
        compMax=max1
    if l1[i]<compMin:
        mini1=l1[i]
        compMin=mini1

print("max element is",max1)
print("min element is",mini1)