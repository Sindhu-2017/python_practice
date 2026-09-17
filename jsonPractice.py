import json
# Q1
user = {
    "name": "Sindhuja",
    "age": 25,
    "role": "QA"
}
js=json.dumps(user)
print(js)
print(type(js))


# Q2
json_data = '{"name": "Sindhuja", "role": "QA"}'

user1=json.loads(json_data)
print(user1["name"])
print(user1["role"])

# Q3
json_data1 = '''
{
    "name": "Sindhuja",
    "skills": [
        "Python",
        "Selenium",
        "Playwright"
    ]
}
'''
user3=json.loads(json_data1)
print(user3["skills"][0])
print(user3["skills"][1])
print(user3["skills"][2])


# Q4
json_data2= '''
{
    "name": "Sindhuja",
    "profile": {
        "role": "QA",
        "experience": 2
    }
}
'''
user4=json.loads(json_data2)
print(user4["profile"]["role"])
print(user4["profile"]["experience"])



# Q5
employee = {
    "name": "Sindhuja",
    "department": "Testing",
    "skills": ["Python", "SQL", "API"]
}
with open("employee.json","w") as file:
    json.dump(employee,file,indent=4)

# Q6
with open("employee.json","r") as file:
    emp=json.load(file)
print(emp["name"])
print(emp["department"])

# Q7
with open("employee.json","r") as file:
    emp1=json.load(file)
emp1["department"]="Automation Testing"

with open("employee.json","w") as file:
    json.dump(emp1,file,indent=4)

# Q8
json_data3 = '''
{
    "status": 200,
    "message": "Login successful",
    "user": {
        "name": "Sindhuja",
        "role": "QA"
    }
}
'''
sts=json.loads(json_data3)
print(sts["status"])
print(sts["message"])
print(sts["user"]["name"])
print(sts["user"]["role"])


# Q9
employee1 = {
    "name": "Sindhuja",
    "department": "Testing",
    "skills": ["Python", "SQL", "API"]
}
str1=json.dumps(employee1)
dict1=json.loads(str1)
print(dict1)
print(type(dict1))

# Q10
test_result = {
    "test_name": "Login Test",
    "expected": "Login successful",
    "actual": "Login successful",
    "status": "PASS"
}
with open("test_result.json","w") as file:
    json.dump(test_result,file,indent=4)
with open("test_result.json","r") as file:
    content=json.load(file)
    print("Test :",content["test_name"])
    print("Expected :",content["expected"])
    print("Actual :",content["actual"])
    print("Status:",content["status"])


