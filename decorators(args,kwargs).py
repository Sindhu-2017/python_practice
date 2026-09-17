# Q1
def test(*args):
    print(args)

test(10, 20, 30)
# (10,20,30)

# Q2
#B

# Q3
def total(*args):
    return args[0]+args[1]+args[2]

print(total(10, 20, 30))

# Q4
def student(**kwargs):
    print(kwargs)

student(name="Sindhuja", age=25)
# {'name': 'Sindhuja', 'age': 25}

# Q5
# C

# Q6
def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["city"])


student(name="Sindhuja", age=25, city="Coimbatore")

# Q7
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, name="Sindhuja", age=25)

# (10, 20)
# {'name': 'Sindhuja', 'age': 25}

# Q8
# def test(*args):  -it accepts any number of positional arguments and collects as tuple
# def test(**kwargs):-it accepts any number of keyword arguments and collects as dictionary

# Q9
numbers = (10, 20, 30)

def add(a, b, c):
    return a + b + c

print(add(*numbers))

# It unpacks the value and send it to the function
# Q10