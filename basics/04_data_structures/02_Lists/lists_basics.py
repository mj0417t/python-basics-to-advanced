#ways to create a list

a=[1,2,3,"sfe",4.5]
print(a) 
a=list("Hello")
print(a)
a=list(('apple','banana','cherry'))
print(a)
a=[2]*5
print(a)

fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(2,'avocado')
print(fruits)
fruits.extend({'guava','pomegranate','kiwi'})
print(fruits)
fruits.remove('cherry')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(4)
print(fruits)
del fruits[1]
print(len(fruits))