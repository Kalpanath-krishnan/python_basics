'''f=open("sample.txt","w")
f.write("hi django")
f.close()


f=open("demo.txt","w")
f.write("new data")
f.close()

f=open("demo1.txt","x")
f.close()
#file append()
f=open("demo.txt","a")
f.write("\n hi python")'''


#with 
with open("demo.txt","r") as file:
    result=file.read()
    print(result)

