# Q1
# pattern = r"\d+"=>it keeps the backslash raw.

# Q2

import re

text = "abc123XYZ"

result = re.findall(r"[A-Z]+", text)

print(result)

# ['XYZ]
# Q3
test="12s34567abd"
regex_negation=re.findall(r"[^0-9]",test)
print(regex_negation)

# Q4
str1="I love Python"
print(re.findall(r"Python|Java",str1))

# Q5
text_group= "Name: Sindhuja, Age: 25"
result_group=re.search(r"Name: (?P<name>\w+), Age: (?P<age>\d+)",text_group)
print(result_group.group("name"))
print(result_group.group("age"))


# Q6
list1=["http://example.com","https://example.com"]
for l in list1:
    if re.fullmatch(r"https?://example.com",l):
        print("Matched")
    else:
        print("Not matched")

# Q7
numbers=[123456,12345,1234567]
for n in numbers:
    if re.fullmatch(r"\d{6}",str(n)):
        print("Match")
    else:
        print("No match")

# Q8
# .* =>it displays all matches 
# .*? =>it displays only the first match

# Q9
test_cases = "TC101 PASS, TC202 FAIL, TC303 PASS"
pattern=re.compile(r"TC\d+")
print(pattern.findall(test_cases))
# Q10
response = """
User ID: USR12345
Transaction ID: TXN98765
Status: PASS
"""
print(re.findall(r"(?:USR|TXN)\d+",response))