limit=int(input("enter the limit"))
list1=[]
list2=[]
for i in range(limit):
    element=int(input())
    list1.append(element)
for i in range(limit):
    element=int(input())
    list2.append(element)
print(list1,list2)

for i in range(len(list1)):
    list1[i],list2[i]=list2[i],list1[i]
print("swapped list",list1,list2)