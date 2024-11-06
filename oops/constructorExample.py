class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(" NAME =",self.name)
        print(" AGE =",self.age)
n=input("enter your name ")
a=input("enter your age ")
obj=Student(n,a)
print(obj.details())

