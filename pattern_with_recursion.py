def pattern(name,line,n=1):
    if n<=line:
        print(name,n)
        n=n+1
        pattern(name,line,n)
name=input("enter name=")
line=int(input("enter number of lines="))
pattern(name,line,n=1)