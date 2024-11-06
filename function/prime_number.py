n=int(input("enter number to check"))
def prime_check(n):
    if n==0 or n==1:
        print("not prime")
        else:
            
    for i in range(1,n):
        if n%i==0:
            print("not prime")
        else:
            print("prime")
prime_check(n)
