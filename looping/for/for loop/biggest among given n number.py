n=int(input("enter the count of numbers"))
biggest=0
for i in range(0,n):
    number=int(input())
    if number>=biggest:
        biggest=number
print(biggest)