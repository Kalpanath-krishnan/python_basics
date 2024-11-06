list1=[]
limit=int(input("enter the limit"))
for i in range(limit):
    n=int(input("enter elements"))
    list1.append(n)
print(list1)
for i in range(0,limit):
    for j in range(1,limit):
        if i==j:
            list1.remove(i)
print(list1) 
