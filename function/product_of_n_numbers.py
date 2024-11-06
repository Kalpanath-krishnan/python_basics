l1=int(input("enter limit"))
list1=[]
for i in range(l1):
    e=int(input("enter numbers"))
    list1.append(e)
list1=tuple(list1)


print(list1)
def products(*list1):
    prod=0
    for i in list1:
        prod*=i
    print("prod =",prod)
products(list1)