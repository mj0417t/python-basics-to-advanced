from collections import OrderedDict
# Create an ordered dictionary
od = OrderedDict()
# Add some key-value pairs
od['apple'] = 1
od['banana'] = 2
od['orange'] = 3
# Print the ordered dictionary
print(od.items())

d2=reversed(list(od.items()))
for k,v in d2:
    print(k,v)

od.popitem(last=False)  # Remove the first item
print(od.items())

od.popitem(last=True)  # Remove the last item
print(od.items())

d=OrderedDict([('x', 10), ('y', 20), ('z', 30)])
d.move_to_end('y')  # Move 'y' to the end
print(d.items())  # Output: OrderedDict([('x', 10), ('z', 30), ('y', 20)])
d.move_to_end('z', last=False)  # Move 'z' to the beginning
print(d.items())  # Output: OrderedDict([('z', 30), ('x', 10), ('y', 20)])

d.pop('z')  # Remove 'z'
print(d.items())  # Output: OrderedDict([('x', 10), ('y', 20)])
d['z'] = 30  # Re-add 'z'
print(d.items())  # Output: OrderedDict([('x', 10), ('y', 20), ('z', 30)])