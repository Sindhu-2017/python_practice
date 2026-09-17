# Q1

with open("test.txt","w") as file:
    file.write("Login Test \n")
    file.write("Search Test \n")
    file.write("Logout Test \n")

# Q2
with open("test.txt","r") as file:
    content=file.read()
    print(content)

# Q3
with open("test.txt","r") as file:
    for line in file:
        print(line)


# Q4
with open("test.txt","r") as file:
    content=file.readlines()
    print(content)

#its returning list

# Q5
with open("result.txt","w") as file:
    file.write("Login: PASS \n")
    file.write("Search: PASS \n")
    file.write("Logout: FAIL \n")

# Q6
with open("result.txt","a") as file:
    file.write("Profile: PASS \n")


# Q7
test_results = [
    "Login: PASS",
    "Search: PASS",
    "Logout: FAIL",
    "Profile: PASS"
]

with open("automation_results.txt","w") as file:
    for result in test_results:
        file.write(result+"\n")

# Q8
test_cases = [
    {"name": "Login", "expected": "Success", "actual": "Success"},
    {"name": "Search", "expected": "Results", "actual": "Results"},
    {"name": "Logout", "expected": "Success", "actual": "Failed"}
]
def find_results(testcase):
    if testcase["expected"] == testcase["actual"]:
       return testcase["name"]+":PASS \n"
    else:
        return testcase["name"]+":FAIL \n"

result=""

for case in test_cases:
     result=result+find_results(case)

with open("automation_results.txt","w") as file:
    file.write(result)
