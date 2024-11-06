num = int(input("Enter a number: "))

i = 1

print("Factors are:")
while i <= num:
    if num % i == 0:
        print(i)
    i += 1  

num=int(input("enter a number : "))
for i in range(1,num,1):
    if num%i==0:
        print(i)
