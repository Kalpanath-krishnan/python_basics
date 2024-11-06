num = int(input("Enter a number: "))
temp=num
i = 1
sum=0

print("Factors are:")
while i < num:
    if num % i == 0:
        print(i)
        sum=sum+i

    i += 1  
print(sum)
if sum==temp:
    print("perfect")
else:
    print("not perfect")

