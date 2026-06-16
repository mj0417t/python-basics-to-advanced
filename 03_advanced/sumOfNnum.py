
n=int(input())
def nSum(n):
    #code here
    ans = 0
    i=1
    while i<=n:
        ans+=i
        i=i+1
    return ans
print(nSum(n))