import heapq
li=[25,15,5,35,10]
heapq.heapify(li)
print(li)  # Output: [5, 10, 15, 35, 25]

heapq.heappush(li,30)
print(li)


h = []
for x in [5, 1, 8, 3]:
    heapq.heappush(h, -x)

print([-x for x in h])


pq = []
heapq.heappush(pq, (2, "Task A"))
heapq.heappush(pq, (1, "Task B"))
heapq.heappush(pq, (3, "Task C"))

print(pq)

print(heapq.heappop(pq))
print(pq)

print(heapq.heappop(pq))
print(pq)

h=[]
for x in[1,3,4,5]:
    heapq.heappush(h,x)
v=heapq.heappop(h)
print(v)
print(h)

a=[(1,'task A'),(3, 'task C'),(2, 'task B')]
heapq.heapify(a)
removedTask=heapq.heappushpop(a,(0,'task d'))
print(removedTask)
print(a)

#finding largest and smallest elems

nums=[1,4,3,5,6,3,6,2]
heapq.heapify(nums)
print('3 largest nums:' , heapq.nlargest(3,nums))
print('2 smallest nums:', heapq.nsmallest(2,nums))

a=[1,-9,-2,-3]
heapq.heapify(a)
print('2 largest: ', heapq.nlargest(2,a, key=abs))

tasks=[(2,'task A'),(1,'task B'),(3,'task C')]
res=heapq.nlargest(2,tasks, key=lambda x: x[0])
print(res)

res = heapq.nsmallest(2, tasks, key=lambda x: x[0])
print(res)

h = [3, 5, 7, 10]
heapq.heapify(h)
removed = heapq.heapreplace(h, 6)

print(removed)
print(h)

#keeping only top 3 score
scores=[45,56,80]
heapq.heapify(scores)
newScore=65
if newScore>scores[0]:
    heapq.heapreplace(scores, newScore)
print(scores)


# Using heapq.merge to merge multiple sorted lists
a=[1,4,6,7,8]
b=[0,1,3,5]
c=[2,7,9]
merged=heapq.merge(a,b,c)
print(list(merged))

#merge with custom key

a=["apple", "cherry", "banana"]
b=["fig", "kiwi", "grape"]
merged=heapq.merge(a,b, key=lambda x: len(x))
print(list(merged))

#merging in reverse order
a=[1,4,6,7,8]
b=[0,1,3,5]
c=[2,7,9]
merged=heapq.merge(a,b,c,reverse=True)
print(list(merged))