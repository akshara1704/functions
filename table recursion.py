def counting(n,i):
    if n==20:
        print("2 * 10 = ",end="")
        return n
    else:
        print("2 *",i,"=",n)
        return counting(n+2,i+1)
print(counting(n=2,i=1))