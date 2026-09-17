# Q1

# greet-it takes the function and we can store in one variable or pass as argument to another dunctiom
#greet()-it calls the greet() function 

# Q2
def greet():
    print("Hello")

def execute(function):
    function()

execute(greet)
# Hello

# Q3
def outer():
    def inner():
        print("Inside inner")
    inner()
outer()

# Q4
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper

def greet1():
    print("hello")

greet1=decorator(greet1)

greet1()

# Q5
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper
@decorator
def greet1():
    print("hello")

greet1()


# Q6
# True

# Q7
def decorator(function):
    def wrapper(a,b):
        print("Function Called")
        result=function(a,b)
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))

# Q8
# *args, **kwargs -explain it

# Q9
# B

# Q10
def login_required(function):
    def wrapper(name):
        function(name)
    return wrapper


@login_required
def welcome(name):
    print(f"Welcome {name}")

welcome("Sindhuja")