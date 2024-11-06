#key value pair :-dictionary
#key cannot be changed but value can reassign

dict1={"name":"aloy","age":39}
print(len(dict1))
print(dict1)
print(dict1["name"])
print(dict1.get("name"))
print(dict1.keys())   #to get all the keys in dictionary
print(dict1.values())   #to get all the values of dictionary
x=dict1.items()
print(x) # to get key and values as tuple elements in a list
dict1.update({"name":"aloy settan"})
print(dict1)
dict1.pop("age")
print(dict1)
dict1.popitem()
print(dict1)
dict1.update({"name:kalpanath"})