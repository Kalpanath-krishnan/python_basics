num = int(input("Enter a number: "))

i = 1
sum=0

print("Factors are:")
while i <= num:
    if num % i == 0:
        print(i)
        temp=i
        sum=sum+i
    i += 1  
print("the sum is",sum)
