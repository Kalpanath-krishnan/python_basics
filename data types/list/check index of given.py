limit=int(input("enter the limit"))
list=[]
for i in range(limit):
    element=int(input())
    list.append(element)
print(list)
check=int(input("enter element to check"))
for i in range(0,limit):
    if list[i]==check:
        print(check,"found at index",i)
        break
else:
    print(check,"not in list")