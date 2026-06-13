a="I'm a string"
upper=lambda x:x.upper()
print(upper(a))

check=lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(check(15))
print(check(-5))
print(check(0)) 

#check odd or even
oddEven=lambda x: 'Even' if x%2==0 else "odd"
print(oddEven(10))
print(oddEven(15))

#list comprehension 
a=[2,3,4,5]
res=[x**2 for x in a]
print(res)

res2=[x for x in a if x%2==0]
print(res2)

b={1,2,3,4,5,6,7,8,9,10}
res=[val for val in b if val%3!=0]
print(res)
res={val for val in b if val%3==0}
print(res)

#creating list from range
lst = [i for i in range(1,11)]
print(lst)

#nested list comprehension
lst=[(x,y) for x in range(1,7) for y in range(3) if (x+y)>=7]
print(lst)

#flattening a matrix
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)

#lamda with list comprehension

lst2=[lambda arg=x: arg*10 for x in range(1,6)]
print(lst2)
for i in lst2:
    print(i())

#used for returning multiple results from a function
def operations(a,b):
    return (lambda: a+b, lambda: a-b, lambda: a*b, lambda: a/b) 

res=operations(10,5)
print(res[0]())

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

#filtre in python

def startWithA(word):
    return word.startswith('a')
fruits = ['apple', 'banana', 'avocado', 'grape', 'apricot']
filtered_fruits = filter(startWithA, fruits)
print(list(filtered_fruits))

x=filter(lambda x: x%2==0, range(1,11))
print(list(x))

b=filter(lambda w: len(w)<=5, fruits)
print(list(b))

#using None as a filter function to remove falsy values from a list
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))

#map() in py
a=['1','2','3','4']
res=list(map(int,a))
print(res)  # Output: [1, 2, 3, 4]

res2=list(map(lambda x: x**3,res))
print("New list: ",res2)

res3 = list(map(lambda x,y:(x,y),res,res2))
print(res3)


#reduce() in py

from functools import reduce
fruits = ['apple', 'banana', 'cherry']
r=reduce(lambda x,y: x+" "+y, fruits)
print(r)

a = [2, 4, 6, 8]
r = reduce(lambda x, y: x + y, a)
print(r)

#largest element in a list using reduce
r = reduce(lambda x, y: x if x > y else y, a)
print(r)

#smallest element in a list using reduce
r=reduce(lambda x,y: x if x<y else y,a)
print(r)

import operator
a = [1, 3, 5, 6, 2]


print(reduce(operator.add, a))
print(reduce(operator.mul, a)) 
print(reduce(operator.add, ["geeks", "for", "geeks"]))

