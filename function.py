#Q1
def greet():
    print("Hello, Welcome to Python!")

greet()

# Q2
def greet(name):
    print(f"Hello {name}")

greet("Sindhuja")

# Q3
def add(a,b):
    return a+b

result=add(10,20)
print(result)

# Q4
def is_even(number):
    if(number%2 == 0):
        return True
    else:
        return False
number=21
if(is_even(number)):
    print("Even")
else:
    print("Odd")


# Q5
def validate_result(expected, actual):
    if expected == actual:
        return "PASS"
    else:
        return "FAIL"

print(validate_result("Login successful", "Login successful"))
print(validate_result("Login successful", "Invalid password"))

#Q6
def validate_status_code(expected, actual):
    if expected == actual:
        return "API TEST PASS"
    else:
        return "APT TEST FAIL"
print(validate_status_code(200, 200))
print(validate_status_code(100, 200))

   
# Q7
def validate_test(test_case):
    if test_case["expected"] == test_case["actual"]:
        return "PASS"
    else:
        return "FAIL"
test_case = {
    "name": "Login Test",
    "expected": "Login successful",
    "actual": "Login successful"
}

print(validate_test(test_case))

# Q8
def calculate_grade(mark):
    if mark<0 or mark>100:
        print("Invalid")
    elif mark>=90:
        print("A")
    elif mark>=75:
        print("B")
    elif mark>=50:
        print("C")
    elif mark>=35:
        print("D")
    else:
        print("Fail")

calculate_grade(102)
calculate_grade(98)
calculate_grade(32)
calculate_grade(75)
calculate_grade(74)


# Q9
def execute_test(test_name, expected, actual):
    print("Test :",test_name)
    if expected ==actual:
        print("Result : PASS")

    else:
        print("Result :FAIL")


execute_test("Login", "Success", "Success")
execute_test("Search", "Results displayed", "No results")
execute_test("Logout", "Logged out", "Logged out")

# Q10
def validate_case(case):
    if case["expected"] == case["actual"]:
        print(case["name"],":PASS")
    else:
        print(case["name"],":FAIL")

test_cases = [
    {"name": "Login", "expected": "Success", "actual": "Success"},
    {"name": "Search", "expected": "Results", "actual": "Results"},
    {"name": "Logout", "expected": "Success", "actual": "Failed"}
]

for cases in test_cases:
    validate_case(cases)

