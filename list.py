#Q1
skills=["Python","Java","Selenium","Playwright","Postman"]
print(skills)

#q2
print(skills[0])
print(skills[-1])

#q3
skills.append("Pytest")

#q4
skills.insert(1,"JavaScript")

#q5
skills.remove("Java")


#Q6
print("Length :",len(skills))

#Q7
if "Selenium" in skills:
    print("Selenium is available")
else:
    print("Selenium is not available")

#Q8
test_results = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "PASS"]
count=0
for result in test_results:
    if result == "PASS":
        count+=1
    else:
        continue
print("Passed Tests =",count)

#Q9
passcount=0
failcount=0
for result in test_results:
    if result == "PASS":
        passcount+=1
    elif result == "FAIL":
        failcount+=1
print("Passed Tests =",passcount)
print("Failed Tests =",failcount)

#Q10
test_cases = [
    "Login",
    "Search",
    "Add to Cart",
    "Checkout",
    "Logout"
]
for case in test_cases:
    print("Executing test :",case)

print(skills)
skills.pop()
print(skills)
skills.pop(1)
print(skills)

print(help(skills))#Q1
skills=["Python","Java","Selenium","Playwright","Postman"]
print(skills)

#q2
print(skills[0])
print(skills[-1])

#q3
skills.append("Pytest")

#q4
skills.insert(1,"JavaScript")

#q5
skills.remove("Java")


#Q6
print("Length :",len(skills))

#Q7
if "Selenium" in skills:
    print("Selenium is available")
else:
    print("Selenium is not available")

#Q8
test_results = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "PASS"]
count=0
for result in test_results:
    if result == "PASS":
        count+=1
    else:
        continue
print("Passed Tests =",count)

#Q9
passcount=0
failcount=0
for result in test_results:
    if result == "PASS":
        passcount+=1
    elif result == "FAIL":
        failcount+=1
print("Passed Tests =",passcount)
print("Failed Tests =",failcount)

#Q10
test_cases = [
    "Login",
    "Search",
    "Add to Cart",
    "Checkout",
    "Logout"
]
for case in test_cases:
    print("Executing test :",case)

print(skills)
skills.pop()
print(skills)
skills.pop(1)
print(skills)
