a=int(input("enter first digit "))
b=int(input("enter second digit "))
print("choose your option")
print(" 1 for addition\n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for exponent")
c=int(input())
if c==1:
    print("answer = ",a+b)
elif c==2:
    print("answer = ",a-b)
elif c==3:
    print("answer = ",a*b)
elif c==4:
    print("answer = ",a/b)
elif c==5:
    print("answer = ",a**b)

else:
    print("Invalid choice")
