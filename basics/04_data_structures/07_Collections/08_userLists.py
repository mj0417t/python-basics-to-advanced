from collections import UserList

ul=UserList([1,2,3,4,5])
print(ul.data)  # Output: [1, 2, 3, 4, 5]

class MyList(UserList):
    # Function to stop deletion
    # from List
    def remove(self, s = None): # type: ignore
        raise RuntimeError("Deletion not allowed")
        
    # Function to stop pop from 
    # List
    def pop(self, s = None): # type: ignore
        raise RuntimeError("Deletion not allowed")
    
# Driver's code
l = MyList([1, 2, 3, 4, 5]) 
print("Original List")
print(l)
l.append(5)
print("After Insertion")
print(l)    
l.remove(2)