limit=int(input("enter limit"))
list=[]
list1=[]
list2=[]
for i in range(0,limit):
    element=int(input())
    list.append(element)
print(list)
for i in list:
    if i%2==0:
     list1.append(i)
    else:
       list2.append(i)
print("even",list1)
print("odd",list2)
