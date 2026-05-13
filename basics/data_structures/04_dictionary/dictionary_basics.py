#creating a dict

a={'x':1,'y':2}
print(a)

b=dict(name="sam", age=30)
print(b)

print(a['x'])
print(b.get('name'))
print(b['name'])

#ADDING ELEM in dix
a['z']=3
print(a)

#updating value

b['name']='Iroha'
print(b)

del a['y']
print(a)

val=a.pop('x')
print(val)
print(a)
print(a.popitem())
print(a)

#iterating through dictionary
d={'A':1,'B':2,'C':3}
for k in d.keys():
    print(k)

k=d.keys()
d['D']=4
print(k)

print(d.values())

for v in d.values():
    print(v)
print(list(d.values()))

print(5 in d.values())

for k,v in d.items():
    print(f"{k}:{v}")

#nested dictionary

record={
    "student 1":{
        'name':"rohan",
        'age':20
    },
    'school':'sjv'
}
print(record)
print(record['student 1']['name'])