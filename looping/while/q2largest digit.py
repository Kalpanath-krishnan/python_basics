

num = int(input("Enter a number: "))


lar = 0


while num > 0:
    digit = num % 10  
    if digit > lar:
        lar = digit  
    num //= 10  


print("The largest digit is:", lar)
