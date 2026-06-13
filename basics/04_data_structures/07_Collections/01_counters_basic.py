from collections import Counter
a=[1,1,1,1,2,3,3,4,5]
cnt=Counter(a)
print(cnt)

#creating a counter
cntr1=Counter([1,2,3,4,3,2,1,4])
cntr2=Counter({1:2,2:3,3:1})
cntr3=Counter('hello')
print(cntr1)
print(cntr2)
print(cntr3)

#accessing counter elements
print(cntr1[1])  # Output: 2
print(cntr1[5])  # Output: 0 (not present, returns 0 instead of KeyError)

#methods of Counter

cntr1.update([1,2,2,3,9])
print(cntr1)  # Output: Counter({2: 5, 1: 3, 3: 3, 4: 2, 9: 1})

cntr1.elements()  # Output: <itertools.chain object at 0x7f8b8c9e5d30>
print(list(cntr1.elements()))  # Output: [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 9]

print(cntr1.most_common(3))  
cntr1.subtract([1,2,2,2,3,3,5,3])
print(cntr1)  # Output: Counter({1: 2, 4: 2, 2: 1, 9: 1, 3: 0, 5: -1})

print(cntr1+cntr2)
print(cntr1-cntr2)
print(cntr1&cntr2)  
print(cntr1|cntr2)


# Creating Counter from a list (sequence of items)  
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# Creating Counter from a dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# Creating Counter using keyword arguments
print(Counter(A=3, B=5, C=2))