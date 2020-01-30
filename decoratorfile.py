def func1():
    print("Welcome To every One")

func2 = func1
del func1
func2()

# This is the concept od Decorator. 
def dec1(func1):
    def dec2():
        print("Executing")
        func1()
        print("Executed")
    return dec2

@dec1
def my_name():
    print("My name is Hanad")

my_name()