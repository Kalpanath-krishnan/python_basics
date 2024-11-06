r=int(input("enter limit"))
for i in range(r,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(2,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()