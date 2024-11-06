print("This is a simple calculator app \n you have 4 choices \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n")
a=int(input("enter a number "))
b=int(input("enter a number "))
def calculator(a,b):
     n=int(input("enter a choice "))
     
     if n==1:
        return(a+b)
     elif n==2:
        return(a-b)
     elif n==3:
        return(a*b)
     elif n==4:
        return(a/b)
     else:
        return("this is wraaaaaaang")

result=calculator(a,b)
print(result)