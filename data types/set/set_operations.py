#union
a={1,2,3,4}
b={"a","b","c",4,3}
c=a.union(b)
print(c)
#update
k={1,2,3,4}
l={"a","b","c",4,3}
k.update(l)
print(k)
#inersection
e=a.intersection(b)
print(e)
#intersection_update
y={1,2,3,4}
z={"a","b","c",4,3}
y.intersection_update(z)
print(y)

#symmetrical_difference
g=a.symmetric_difference(b)
print(g)
#symmetric_differnce_update
a.symmetric_difference_update(b)
print(a)

