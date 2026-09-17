# Q1
numbers = [10, 20, 30, 40]

iterator=iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(iterator.__next__())


# Q2
# print(iterator.__next__())
# it shows an error with StopIteration

# Q3
# list is an iterable because we can go through the values one by one

# Q4
iterator = iter([1, 2, 3])
print(iterator)
# iterator and iterable
 

# Q5
#iter()=> user to create a iterator
#next()=>used to get the next value of iterator

# Q6
numbers = [5, 10, 15]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Q7
numbers = [1, 2]

it1 = iter(numbers)

print(next(it1))
print(next(it1))
# print(next(it1))

#it shows error because we are trying to access item which is not there

# Q8
# iterable-is an object whose value can be through one by one
# iterator-remembers its current position and return one value at a time
