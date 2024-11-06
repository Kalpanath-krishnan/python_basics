class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_details(self):
        print(f"name:{self.name} \n age:{self.age}")

class Student(Person):
    
         
