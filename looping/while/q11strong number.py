n=int(input("enter a number"))
temp=n

sum=0
while n!=0:
    digit=n%10
    fact=1
    print(digit)
    while digit>1:
        fact=fact*digit
        print(fact)
        digit=digit-1
    sum=sum+fact
    n=n//10
print(sum)
if temp==sum:
    print("yes its a strong")
else:
    print("noo its not")
