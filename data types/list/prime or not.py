n=int(input("enter limit"))
list=[]
list1=[]
list2=[]

for i in range(n):
 j=int(input())
 list.append(j)
print(list)
for i in list:
 for j in range(2,len(list)):
  if j%i==0:
   list1.append(i)
else:
   list2.append(i)
print(list1)
print(list2)

  
 