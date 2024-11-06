#occurance of character
list=["a","s","d","f","a","c","b","b","b"]
a=input("enter character to find")
count=0
for i in list:
    if i==a:
        count+=1
print(count)
