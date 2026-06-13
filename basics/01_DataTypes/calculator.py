a,b=input().split()
a=int(a)
b=int(b)
operator=int(input())
def calculate(a: int, b: int, operator: int) -> None:
    # code here
    match operator:
        case 1:
            print(a+b, end=" ")
        case 2:
            print(b-a, end=" ")
        case 3:
            print(a*b, end=" ")
        case _:
            print("Invalid Input", end=" ")


print(calculate(a,b,operator))