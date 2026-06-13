#ways to create a tuple

a=()
print(a)
a=('f',)
print(a)
a=('f','g','h')
print(a)

a=(5, 'welcome', 3.14, [1, 2, 3], (4, 5),{'key': 'value'})
print(a)

#access tuple elements
tup=tuple("geeks")
print(tup)
print(tup[0])  # Output: 'g'
print(tup[1:4])  # Output: ('e', 'e', 'k')
print(tup[-1])  # Output: 's'
print(tup[:3])

tup=("Geeks", "for", "Geeks")
a,b,c=tup
print(a)  # Output: 'Geeks'
print(b)  # Output: 'for'           
print(c)  # Output: 'Geeks'

#tuple concatenation
tup1=(0,1,2,3)
tup2=('zero','one','two','three')
tup3=tup1+tup2
print(tup3)

#slicing of tuple
print(tup3[1:4:2])
print(tup3[::2])
print(tup3[::-1]) #reverse the tuple
print(tup3[-1:-5:-1])
print(tup3[4:9])

del tup3

tup=(1,2,3,4,5)
print(len(tup)) 
a,b,*c=tup
print(a)  # Output: 1
print(b)
print(c)

