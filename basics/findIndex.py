arr = tuple(map(int, input().split()))
x = int(input())

i=0
while i<len(arr):
    if arr[i]==x:
        print(i)
        break
    i=i+1