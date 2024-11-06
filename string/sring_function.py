a=input()
rev=""
for i in a:
    rev=i+rev
if rev==a:
    print("yes palindrome")
else:
    print("no its not palindrome")