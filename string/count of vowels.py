string1=input("enter any string")
vowels="a,e,i,o,u"
string2=string1.lower()
count=0
for i in string2:
    for j in vowels:
        if j==i:
            count+=1

print("no of vowels in input= ",count)