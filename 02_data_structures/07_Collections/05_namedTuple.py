from collections import namedtuple

#declaring naemdtuple
Student=namedtuple('Student',['name','age','grade'])

#adding values
a1=Student('Niharika',26,'A')
a2=Student('Sonam', 24,'B')

#accessing values
print(a1)  # Output: 'Student'
print(a1.name)  # Output: 'Niharika'
print(a1.age)   # Output: 26    
print(a1.grade) # Output: 'A'
print(a2[1])  # Output: 24

#creating a namedTuple
Point=namedtuple('Point',['x','y'])
p1=Point(x=2,y=3)
print(p1)  # Output: 'Point(x=2, y=3)'
print(p1.x)  # Output: 2

print(getattr(p1,'y'))  # Output: 3
print(hasattr(p1,'z'))  # Output: False

#conversion using _make()

a3=['Ruhan',21,'A+']
a4={"name":'Suhail', "age":22, "grade":'S+'}

print(Student._make(a3))  # Output: Student(name='Ruhan', age=21, grade='A+')
print(Student._make(a4.values()))  # Output: Student(name='Suhail', age=22, grade='S+')

#conversion using _asdict()
# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(Student._asdict(a2))

print(Student(**a4)) #to convert a dictionary to namedtuple using unpacking operator **, Output: Student(name='Suhail', age=22, grade='S+')

print("All the fields in Student namedtuple are: ", Student._fields)  # Output: ('name', 'age', 'grade')
a5=a2._replace(name='Sahil')
print(a5) # Output: Student(name='Sahil', age=24, grade='B')
print(a2) # Output: Student(name='Sonam', age=24, grade='B') (original namedtuple remains unchanged)

print(Student.__new__(Student, 'Ruhan', 21, 'A+'))  # Output: Student(name='Ruhan', age=21, grade='A+')

print(p1.__getnewargs__())  # type: ignore # Output: (2, 3) (returns a tuple of the field values in the order they were defined)