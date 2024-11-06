#largest in list
n=int(input("enter limit"))
list=[]
large=0
for i in range(n):
 j=int(input())
 list.append(j)
print(list)
for i in list:
  if i>=large:
    large=i
print(large)
