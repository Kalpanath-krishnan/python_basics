t=(1,2,3,4,5)
b=list(t)
temp=[]
print(b)
for i in range(len(b)):
    element=b[i]
    print(element)
    for i in temp:
        temp.insert(i,element)
print(temp)
