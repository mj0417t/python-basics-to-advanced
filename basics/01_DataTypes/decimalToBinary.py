n=int(input())
def decToBinary(n):
    ans = ""
    while n>0:
        ans=str(n%2)+ans
        n=n//2
    return ans
print(decToBinary(n))