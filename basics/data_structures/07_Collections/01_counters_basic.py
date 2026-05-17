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
