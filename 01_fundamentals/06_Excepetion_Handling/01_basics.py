n=10
try:
    res =n/0
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print(f'Result is {res}')
finally:
    print("Execution completed")


a=['10','twenty',30]
try:
    total=int(a[0])+int(a[1])
except (ValueError, TypeError) as e:
    print("Error", e)
except IndexError:
    print("Index out of range")

