class MyCustomError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message, error_code):
        self.message = message
        self.error_code=error_code
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
    

def divide(a,b):
    if b==0:
        raise MyCustomError("Division by zero is nor allowrd",400)
    return a/b

try:
    res=divide(10,0)
except MyCustomError as e:
    print(f'Caught an error:{e}')

# eg-2

class FileProcessError(Exception):
    def __init__(self, message,filename, lineno):
        super().__init__(message)
        self.message=message
        self.filename=filename
        self.lineno=lineno
    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.lineno}"
    
try:
    raise FileProcessError("Syntax error",'abc.txt',13)
except FileProcessError as e:
    print(f"Caught an error:{e}")

# NetworkError has base RuntimeError and not Exception
class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = (arg,)   # store as tuple

try:
    raise NetworkError("Connection failed")
except NetworkError as e:
    print(e.args)
        