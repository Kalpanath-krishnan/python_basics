#sum of n natural numbers

num=int(input("enter a number : "))
sum=0
for i in range(0,num,1):
   sum+=i
print("sum of ",num,"natural number = ",sum)
