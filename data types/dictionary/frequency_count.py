list1=[1,1,1,2,3,4,3,2,5,6]
dict1={}
for i in list1:
    count=0
    for j in list1:
        if i ==j:
            count+=1 
        dict1[i]=count
print(dict1)
