n=int(input("Enter a number:   "))
def fibonacciNumbers(  n):
        # code here
        def fibo(num):
            if num==0:
                return 0
            if(num==1):
                return 1
            n1=fibo(num-1)
            n2=fibo(num-2)
            return n1+n2
        x=[]
        for i in range(0,n+1):
            x.append(fibo(i))
        return x

print(fibonacciNumbers(n))