def table(n,i):
    if n<=n*10 and i<=10:
        print(n,"*",i,"=",n*i)
        i=i+1
        table(num,i)
num=int(input("enter number you want the tablr="))
table(num,1)