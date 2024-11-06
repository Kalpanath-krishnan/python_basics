#smallest in list
n=int(input("enter limit"))
list=[]
small=1
for i in range(n):
 j=int(input())
 list.append(j)
print(list)
for i in list:
  if i<small:
    small=i
print(small)
