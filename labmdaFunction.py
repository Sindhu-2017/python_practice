# Q1
add=lambda a,b:a+b
print(add(10,20))

# Q2
square=lambda s:s*s
print(square(6))

# Q3
type_check=lambda n:"Even" if n%2 ==0 else "Odd"
print(type_check(10))
print(type_check(7))

# Q4
numbers = [1, 2, 3, 4, 5]
powers=list(map(lambda n:n*2,numbers))
print(powers)

# Q5
squares=list(map(lambda n:n*n,numbers))
print(squares)

# Q6
numbers1 = [2, 5, 7, 3, 9, 1, 8]
greater_numbers=list(filter(lambda n:n>5,numbers1))
print(greater_numbers)

# Q7
numbers2 = [1, 2, 3, 4, 5, 6, 7]
odd=list(filter(lambda n:n%2 ==1 ,numbers2))
print(odd)

# Q8
students = [
    ("John", 80),
    ("Alice", 95),
    ("Bob", 70)
]
sorted_students=sorted(students,key=lambda student:student[1])
print(sorted_students)

# Q9
employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 70000},
    {"name": "C", "salary": 40000}
]
sorted_employees=sorted(employees,key=lambda emp:emp["salary"],reverse=True)
print(sorted_employees)


# Q10
# map()=>it applies function to all the items in a list
# filter()=>it keeps items which are all satisfy the particular condition