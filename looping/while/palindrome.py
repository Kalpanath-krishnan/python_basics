#reverse a number
input_number=int(input("enter your input"))
temp=input_number
reverse=0
while input_number>0:
    digit=input_number%10
    reverse=reverse*10+digit
    input_number=input_number//10
    

print(reverse)
if temp==reverse:
    print("yes its palindrome")
else:
    print("noo its not a palindrome")
