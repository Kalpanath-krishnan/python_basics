#reverse a number
input_number=int(input("enter your input"))
reverse=0
while input_number>0:
    digit=input_number%10
    reverse=reverse*10+digit
    input_number=input_number//10
if reverse==input_number:
       print("yes its palindrome")  
else:
    print("no its not palindrome")
