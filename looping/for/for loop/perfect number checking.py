n=int(input("give number to check perfect ror not"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not perfect number")