import numpy as np
a=np.array([1,2,3,4])
print(a*2)


#multidimensional arr
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]

arr=np.array(l2)
print("Numpy single-dim array in Python\n",arr)

arr=np.array([l1,l2,l3])
print("Numpy multi-dim array in Python\n",arr)

b=np.array([[0,4,2],
            [3,4,5],
            [23,4,5],
            [2,34,5],
            [5,6,7]
            ])
print("Shape of arr: ",b.shape)
print("Rank of arr: ")

#dtype
arr1=np.array([2,3,45])
arr2=np.array([0.2,.5,.9])
print(arr1.dtype)
print(arr2.dtype)

#using fromiter

var="geeksforgeeks"
arr=np.fromiter(var, dtype='U2')
print("fromiter() array: ",arr)

#using arange() fn
arr=np.arange(1,20,2,dtype=np.float32)
print(arr)

#using linspace()
arr=np.linspace(3.5,10,3,dtype=np.int32)
print(arr)

#using empty()
arr=np.empty([4,3], dtype=np.int32)
print(arr)

arr=np.ones([4, 3],
        dtype = np.int32,
        order = None)
print(arr)

arr=np.zeros([3,3],dtype=np.float32)
print(arr)