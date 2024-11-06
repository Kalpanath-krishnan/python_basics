class Salary:
    def __init__(self,name,code,bs):
        self.name=name
        self.code=code
        self.bs=bs
        self.da=bs*.05
        self.hra=bs*.051
        self.pf=bs*.01
        self.net=bs+self.da+self.hra-self.pf
    def display(self):
        print("name :",self.name)
        print("employee code :",self.code)
        print("basic salary :",self.bs)
        print("DA :",self.da)
        print("PF :",self.pf)
        print("HRA :",self.hra)
        print("NET SALARY :",self.net)
name=input("enter your name")
code=input("enter your employee code")
bs=int(input("enter your basic salary"))
obj=Salary(name,code,bs)
print(obj.display)

