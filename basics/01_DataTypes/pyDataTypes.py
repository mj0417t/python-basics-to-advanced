x=24
print(type(x))
x=65.34
print(type(x))
x="Hello World"
print(type(x))
x=["rose", "tulip","lotus","sunflower"]
print(type(x))
x=("bat","ball","wickets")
print(type(x))

a=34
print(type(a))
b=34.34
print(type(b))
c=2+4j
print(type(c))

#string 
s="hello world"
print(s)
print(s[1])
print(s[-1])
print(s[0])

#list
x=[1,2,3,"fos",'sof']
print(type(x))

#tuple
y=(1,2,3,"fos",'sof')
z=(1,)
print(type(y))
print(type(z))

#set
s1=set()
s1=set("hello world") #using string
s2=set(["geeks","for","geeks"])
print(s1)
print(s2)

for i in s1:
    print(i,end=" ")

print("geeks" in s2)

#dictionary
d1={}
d2={1:"john",2:34,3:"new york"}
print(d1, type(d1))
print(d2, type(d2))

d3=dict(name="john",age=34,city="new york")
print(d3, type(d3))

print(d2[1])
print(d3["name"])
print(d2.get(2))
print(d3.get("age"))
