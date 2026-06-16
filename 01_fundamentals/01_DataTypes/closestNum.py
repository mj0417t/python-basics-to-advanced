n,m=input().split()
n=int(n)
m=int(m)
def closestNum(n,m):
    closest=0
    min_diff=float('inf')
    for i in range(n-abs(m),n+abs(m)+1):
        if(i%m==0):
            diff=abs(n-i)
            if diff<min_diff or (diff==min_diff and abs(i)<abs(closest)):
                min_diff=diff
                closest=i
    return closest

def closestNumOpt(n,m):
    q=int(n/m)
    n1=q*m #closest multiple of m less than or eq to n
    #second closest multiple of m
    if(n<0 and m>0) or (n>0 and m<0):
        n2=(q-1)*m 
    else:
        n2=(q+1)*m
    if abs(n-n1)==abs(n-n2):
        return n1 if abs(n1)>abs(n2) else n2
    else: 
        return n1 if abs(n-n1)<abs(n-n2) else n2
print(closestNum(n,m))
print(closestNumOpt(n,m))