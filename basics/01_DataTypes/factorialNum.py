num=int(input("enter a number: "))
def factorial( n: int) -> int:
    # code here
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans

print("Factorial of", num, "is ",factorial(num))