l = int(input("Enter the start limit: "))
u = int(input("Enter the end limit: "))

for i in range(l, u + 1):
    if i == 1:  # Skip 1, since it's not a prime number
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)  # This is part of the else block for the inner loop
