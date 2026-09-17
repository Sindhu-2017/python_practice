# Q1
def numbers():
    yield 10
    yield 20
    yield 30
num=numbers()
print(next(num))
print(next(num))
print(next(num))

# Q2
# return - it will give the result and terminate the function
# yield - it will produce one value at a time and pauses an execution in that position

# Q3
def test():
    yield 10
    yield 20
    yield 30

gen = test()

print(next(gen))
print(next(gen))

#10
#20

# Q4
def count_up_to(n):
    for i in range(1,n+1):
        yield i

count=count_up_to(5)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))


# Q5
def count_up_to(n):
    for i in range(1,n+1):
        yield i

for number in count_up_to(5):
    print(number)

# Q6
squares=(x*x for x in range(1,6))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# Q7
# B

# Q8
# True

# Q9
# Generator is useful when we are dealing with large data.It makes code more readable and produces one value at a time

# Q10
def even_numbers(n):
    for i in range(1,n+1):
        if i%2 ==0:
            yield i

even=even_numbers(10)
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))

