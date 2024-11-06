try:
    n=int(input("enter a number "))
    n1=int(input("enter a number "))
    c=n1/n
except ZeroDivisionError:
    print("plese enter a non zero integer next time")
except ValueError:
    print("please enter an integer next time")
else:
        print(f" result={c}")
finally:
     print("hi   .....")