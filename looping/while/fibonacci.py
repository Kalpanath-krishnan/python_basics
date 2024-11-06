n=int(input("how many elements you need ? "))
a=0
b=1
i=0
while i<=n:
    next=a+b
    print(next)

    a=b
    b=next
    i=i+1
