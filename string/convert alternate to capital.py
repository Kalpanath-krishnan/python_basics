string1=input("enter any string")
result=""

for j in range(len(string1)):
    if j%2==0:
        result+=string1[j].upper()
    else:
        result+=string1[j].lower()
print(result)