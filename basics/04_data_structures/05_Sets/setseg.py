s={10,20,30}
print(s)
print(type(s))

s=set(['a','b','c','a'])
s.add('e')
print(s)

#frozen set
a=frozenset([1,2,3,4])
b=frozenset([3,4,5,6])
c=a.copy()
print(c)

print("Union: ",a.union(b))
print("Intersection: ",a.intersection(b))
print("Difference: ",a.difference(b))
print("Symm diff: ",a.symmetric_difference(b))


