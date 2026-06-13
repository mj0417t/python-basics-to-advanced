def func1():
    print("This is func1")
    a=45
    def func2():
        print("This is func2")
        nonlocal a # allows us to modify the variable 'a' defined in the enclosing scope (func1)
        a=54
        print("Value of a in func2 after assignment is: ",a)
    func2()
    print("Value of a in func1 is: ",a)
func1()
