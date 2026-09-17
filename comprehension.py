# Q1
list1=[x for x in range(1,6)]
print(list1)

# Q2
numbers = [1, 2, 3, 4, 5]
squares=[n*n for n in numbers]
print(squares)


# Q3
numbers1 = [10, 15, 20, 25, 30]
even=[n for n in numbers1 if n%2 ==0]
print(even)

# Q4
names = ["sindhuja", "python", "automation"]
upper_names=[name.upper() for name in names]
print(upper_names)

# Q5
numbers2 = [1, 2, 3, 4, 5]
types=["Even" if n%2 == 0 else "Odd" for n in numbers2]
print(types)

# Q6
dict1={x:x*x for x in range(1,6)}
print(dict1)

# Q7
set1={1, 2, 2, 3, 3, 4, 5}
print(set1)

# Q8
#[x for x in numbers] -it displays all the numbers in the numbers list

# [x for x in numbers if x % 2 == 0]-it displays only even numbers in the list

# Q9
numbers_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares={x:x*x for x in numbers_list1 if x%2 ==0}
print(even_squares)