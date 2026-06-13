from collections import deque
# Create a deque
d = deque()
# Add elements to the right end 
d.append(1)
d.append(2)
print(d)  # Output: deque([1, 2])
# Add elements to the left end
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2])    

#creating a deque with a list
dq=deque([4,5,6,7,8])
print(dq)  # Output: deque([4, 5, 6, 7, 8])

#accessing items in a deque
print(dq[0])  # Output: 4
print(dq[-1])  # Output: 8

dq.extend([8,9,10])
print(dq)

dq.extendleft([1,2,3])
print(dq)

dq.remove(8)
print(dq)
dq.pop()  # Remove and return the rightmost element
print(dq)   

dq.popleft()
print(dq)

print(len(dq))

print(list(dq))  # Convert deque to a list
print(dq.count(8))  # Count occurrences of 8 in the deque
dq.reverse() # Reverse the deque in-place
print(dq)  # Output: deque([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

dq.rotate(2)  # Rotate the deque to the right by 2 steps
print(dq)  # Output: deque([2, 1, 10, 9, 8, 7, 6, 5, 4, 3])
dq.rotate(-3)  # Rotate the deque to the left by 3 steps    
print(dq)  # Output: deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])

dq.clear()  # Remove all elements from the deque
print(dq)  # Output: deque([])  

dq.extend([1,2,3,4,5])
print(dq)  # Output: deque([1, 2, 3, 4, 5])
dq.rotate(1)  # Rotate the deque to the right by 1 step 
print(dq)  # Output: deque([5, 1, 2, 3, 4])