#1.add set of elements to a set
a={"c","g"}
b=[1,2,"a","f"]
a.update(b)
print(a)
#2.return identical elements
a={"c","g","a"}
b={1,2,"a","f"}
c=a.intersection(b)
print(c)
#3.return unique items
a={"c","g","a"}
b={1,2,"a","f"}
c=a.symmetric_difference(b)
print(c)
#4.update first set with elements that doesnot exist in second set
a={"c","g","a"}
b={1,2,"a","f"}
a.symmetric_difference_update(b)
print(a)
#5.remove items from list at once
a={"c","g","a"}
a.clear()
print(a)
#6.return set of elements present in either a or b but not in both
a={"c","g","a"}
b={1,2,"a","f"}
c=a.symmetric_difference(b)
print(c)
#7check if two sets have common elements display if any
a={"c","g","a"}
b={1,2,"a","f"}
c=a.intersection(b)
print(c)
#8 updsate set 1 by adding items from set2 except common items
a={"c","g","a"}
b={1,2,"a","f"}
a.update(b)
print(a)
#9remove elemets from set 1 that are not common in both 1 ND 2
a={"c","g","a"}
b={1,2,"a","f"}
a.symmetric_difference_update(b)
print(a)


