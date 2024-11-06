#sum of n elements
n=int(input("enter limit"))
list=[]
sum=0
for i in range(n):
 j=int(input())
 list.append(j)
print(list)
for i in list:
  sum+=i
print(sum)
