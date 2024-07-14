length=int(input("enter no of items in the list="))
l1=[]
for i in range(0,length):
    items=int(input("enter no="))
    l1.append(items)
print("list items",l1)
def sorting(a):
    a.sort()
    print("sorted list",a)
    smallest=a[0]
    print("smallest=",smallest)
    greatest=a[-1]
    print("greatest=",greatest)
sorting(l1)