n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        factor=i
        sum+=i
print(sum)
