#Q1-tuple
browsers = ("Chrome", "Firefox", "Edge", "Safari")
print(browsers)
print(browsers[0])
print(browsers[-1])

#Q2
# browsers[0]="Brave"
#TypeError: 'tuple' object does not support item assignment

# Q3 — Set
results = {"PASS", "FAIL", "PASS", "PASS", "FAIL"}
print(results)

# Q4
results.add("SKIPPED")
print(results)

# Q5 — Set operations
expected = {"username", "password", "email"}
actual = {"username", "password", "phone"}

print("Missing fields :",expected - actual)
print("Unexpected fields :",actual-expected)


# Q6 — Dictionary
user = {
    "name": "Sindhuja",
    "role": "Tester",
    "experience": 1
}

print(user["name"])
print(user["role"])

# Q7
user["status"]="Active"
print(user)

# Q8
user["role"]="Automation Tester"
print(user)

#Q9
for key,value in user.items():
    print(key,"=",value)
# Q10
test_case = {
    "id": 101,
    "name": "Login Test",
    "expected": "Login successful",
    "actual": "Login successful",
    "status": "PASS"
}

if test_case["expected"]==test_case["actual"]:
    print("Test PASS")
else:
    print("Test FAIL")