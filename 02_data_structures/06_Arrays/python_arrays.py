import array as ar
arr=ar.array('i',[1,2,3])
print(arr[0])
arr.append(5)
print(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

print('\n',*arr)

#unpacking arrays

a,b,c,d=arr
print(a,b,c,d)

a,*b,c=arr
print(a,b,c)

arr1=ar.array('i',[1,2])
arr2=ar.array('i',[3,4])
arr3=[arr1,arr2]
(a,b),(c,d)=arr3
print(a,b)
print(c,d)

arr=ar.array('i',[10,20,30,40,50])
a,*b=arr[:2],arr[2:]
print(a,b)

arr.remove(10)
print(arr)

arr.pop()
print(arr)

arr.pop(2)
print(arr)

#array slicing
a=[1,2,3,4,5,5,6,66,7,8,0,9]
b=ar.array('i',a)

res=b[3:8]
print(res)

res=b[5:]
print(res)

res=b[:]
print(res)
print(a.index(3))
print(a.count(4))
a.reverse()
print(*a)