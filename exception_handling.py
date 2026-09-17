# Q1
try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print("Number cannot be divided by zero")

# Q2
try:
    num=int("abc")

except ValueError:
    print("Invalid number")
    
# Q3
try:
    age=int(input("Enter youe age :"))
    print(age)
except ValueError:
    print("Please enter a valid age")


#Q4— Multiple Exceptionss
try:
    num1=int(input("Enter the dividend:"))
    num2=int(input("Enter the divisor:"))
    result=num1/num2
    print(result)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("The number cannot be divided by zero")


# Q5-else
try:
    num=int("100")
except ValueError:
    print("Invalid")
else:
    print("Conversion successful")

#because 100 was coverted to int and there is no error .so else part was executed

# Q6-finally
try:
    r1=10/0
    print(r1)
except ZeroDivisionError:
    print("Error occured")
finally:
    print("Program Completed")


# Q7
response = {
    "status_code": 200,
    "message": "Login successful"
}
try:
    if response["status_code"] == 200:
        print("API TEST PASS")

except KeyError:
    print("Its not a valid key")
finally:
    print("API validation completed")


# Q8 Missing API Field
response1 = {
    "message": "Login successful"
}
try:
    print(response1["status_code"])

except KeyError:
    print("Status code is missing")

# Q9— QA Validation Function


def validate_status(response):
    try:
        if response["status_code"] == 200:
            print("PASS")
        else:
            print("FAIL")
    except KeyError:
        print("STATUS CODE MISSING")

validate_status({"status_code": 200})
validate_status({"status_code": 404})
validate_status({})

# Q10
test_cases = [
    {"name": "Login", "status_code": 200},
    {"name": "Search", "status_code": 200},
    {"name": "Logout", "status_code": 500},
    {"name": "Profile"}
]

def validate_api_test(test_case):
    try:
        if test_case["status_code"]==200:
            print(test_case["name"],":PASS")
        else:
            print(test_case["name"],":FAIL")
    except KeyError:
        print(test_case["name"],":STATUS CODE MISSING")

for case in test_cases:
    validate_api_test(case)


