counter=2
number=int(input("enter number= "))
def prime(number):
    if number==1:
        print("number is prime number")
    elif number==2:
        print("number is a prime number")
    else:
        for i in range(2,number):
            if number%i==0:
                print("number is not a prime number")
                break
            counter=counter+1
            if counter==number:
                 print("number is a prime number")
prime(number)