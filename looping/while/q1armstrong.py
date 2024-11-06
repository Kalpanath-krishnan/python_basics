#armstrong
n=int(input("enter a number"))
length=len(str(n))
temp=n
sum=0

while temp!=0:
    digit=temp%10
    sum+=digit**length
    temp=temp//10
    
if sum==n:
    print("yes its armstrong")
else:
    print("no its not")
