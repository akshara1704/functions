num=int(input("enter number to print multiple="))
count=0
for i in range(10,80):
    if i%num==0:
        count=count+1
        print(i)
print("ther are",count,"multiples of",num)