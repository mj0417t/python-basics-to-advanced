str="GeeksforGeeksSinceDay1"
print(str[0])
print(str[-4])
print(str[4:8])
print(str[:5])
print(str[5:])
print("Traversing the string")
for char in str:
    print(char, end=" ")

#deleting a string
del str

#updating string
str = "hello world    "
s1 = "H"+str[1:]
s2 = str.replace("world", "Python")
print(str)
print(s1)
print(s2)
print(len(s1))
print(s1.upper())
print(s2.lower())
print(str.strip())
print(s1.title())
print(s2.swapcase())
print(s1.capitalize())

s="Hello "
print(s*3)

name="raj shamani"
age=22
print(f"Hello, My name is {name} and I'm {age} yrs old")

import datetime
today = datetime.datetime.today()
print(f"Today's date is: {today:%B-%d-%Y}")


eng,hin,maths=78,65,85
print(f"Ram got total marks {eng+hin+maths} and average marks {(eng+hin+maths)/3:.2f}")

#using format method
a="musarrat"
b=25
msg="My name is {0} and I'm {1} yrs old".format(a,b)
print(msg)

print("\a")

product, brand, price, issue, effect = "SmartPhone", "Apple", 999, "overheating", "battery drain"
print("{:<20} is a popular brand".format(brand))
print("They have a {} for {} ruppees".format(product,price))
print("I wonder why the program was {} me-turns out it was a {}".format(effect,issue))
print("Truncated product name: {:.5}".format(product))

print("The issue is {:.6f}% solved {}!!".format(100,"easily"));

print("My avg of this {} was {:.2f}%".format("semester", 85.6789))

print("My avg of this {} was {:.0f}%".format("semester", 85.6789))

print("The {} of 100 is {:b}".format("binary", 100))
print("The {} of 100 is {:o}".format("octal", 100))
print("The {} of 100 is {:x}".format("hexadecimal", 100))

def formatted_table(a,b):
    for i in range(a, b):
        print("{:6d} {:6d} {:6d}".format(i, i**2, i**3))

formatted_table(3, 11)

d = {"first_name": "Tony", "last_name": "Stark", "aka": "Iron Man"}
print("My name is {first_name} {last_name}, also known as {aka}.".format(**d))

a=[100.453454356, 17.3435345, 60.42342, 300.43543524543]
b=['{:.2f}'.format(elem) for elem in a]
print(b)