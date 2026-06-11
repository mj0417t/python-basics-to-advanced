from collections import ChainMap
d1={'a': 1, 'b': 2}
d2={'c': 3, 'd': 4}
cm = ChainMap(d1, d2)
print(cm['a'])  # Output: 1 (from d1)
print(cm['c'])  # Output: 3 (from d2)       
print(cm.keys())

print("All chainMap contents are:" , cm.maps)
print("All chainMap items are:" , cm.items())
print("All chainMap values are:" , cm.values())
print("All chainMap keys are:" , cm.keys())

# Modifying the ChainMap
d3={'e': 5,'f':2,'g':5}
cm2=cm.new_child(d3)  # Add d3 to the front of the ChainMap
print(cm)
print(cm2)
cm2.maps=reversed(cm2.maps)  # Reverse the order of the maps in cm2
print(cm2)