a=int(input("enter the current reading"))
b=int(input("enter the previous reading"))
consumption=a-b
print("your consumption = ",consumption)

slab1=(consumption-100)
slab2=slab1-50
slab3=slab2-50
slab4=slab3-50

amount=(slab1*0.5)+(slab2*0.75)+(slab3*1)+(slab4*2)
print("your bill amount= ",amount)
