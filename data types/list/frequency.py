limit=int(input("enter limit "))
list1=[]
for i in range(1,limit+1):
    element=int(input())
    list1.append(element)
l2=[]
for i in list1:
    if i not in l2:
        l2.append(i)
print(l2)
for i in l2:
    c=0
    for j in list1:
        if i==j:
            c+=1
    print (i, " in ",c," times ")