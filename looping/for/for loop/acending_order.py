n=int(input("enter limit"))
list=[]
ascend=[]
for i in range(0,n):
    e=int(input())
    list.append(e)
print(list)

for i in range(0,n):
    for j in range(0,i):
     if list[i]<list[j]:
        t=list[j]
        list[i]=list[j]
        list[j]=t
print(list)





