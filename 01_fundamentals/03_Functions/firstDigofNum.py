num=int(input("Enter a number:   "))
def firstDigofNum(num):
    while num >= 10:
        num //= 10
    return num

print(firstDigofNum(num))