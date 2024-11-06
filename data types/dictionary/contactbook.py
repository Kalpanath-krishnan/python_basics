print(" 1.Add a contact \n 2.Delete a contact \n 3.Edit a contact \n 4.Search a contact \n 5.List all contacts \n 6.Exit")
dict1={}
while True:
    n=int(input("enter your choice \n"))
    if n==6:
        break
    elif n==1:
        name=input("enter name \n")
        number=input("enter contact number \n")
        dict1[name]=number
        
        print("1 contact added successfully")
    elif n==3:
        name=input("enter name to edit \n")
        number=input("enter number to edit")
        dict1[name]=number
    elif n==2:
        x=input("enter name to delete")
        dict1.pop(x)
        print("contact deleted")
    elif n==4:
        x=input("enter name to search")
        print(dict1[x])
    elif n==5:
        print("name\t\t\t\t\t\t\t number")

        for x,y in dict1.items():
            print (x,"\t\t\t\t\t\t\t",y)   
    else:
        break 
       











