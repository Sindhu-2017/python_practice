# Q1
import re

text = "My age is 25"

result = re.search(r"\d+", text)

print(result.group())
# 25

# Q2

text_python = "I am learning Python"
if re.search("Python",text_python):
    print("Found")

else:
    print("Not Found")


# Q3
# re.search()=>Check pattern anywhere in the string
# re.match() => checks only the beginning of the string

# Q4
text_numbers= "I bought 2 pens, 5 books and 10 pencils"
print(re.findall(r"\d+",text_numbers))

# Q5
text_case = "TC101 PASS, TC102 FAIL, TC103 PASS"
print(re.findall(r"TC\d+",text_case))


# Q6
numbers=[12345,1234,123456]
for n in numbers:
    if re.fullmatch(r"\d{5}",str(n)):
        print("Match")
    else:
        print("No match")

# Q7
text_replace = "User123 has 500 points"
print(re.sub(r"\d+","xxx",text_replace))

# Q8
text_extract = "Name: Sindhuja, Age: 25"
result=re.search(r"Name: (\w+), Age: (\d+)",text_extract)
print(result.group(1))
print(result.group(2))


# Q9
# \d=>pattern  can contain one digit
# \d+ =>the pattern can contain one or more digits
# \d{3} =>the pattern should contain exactly 3 digits

# Q10
log = """
Login successful
Transaction ID: TXN12345
Status: PASS
"""

print(re.findall(r"TXN\d+",log))


# <re.Match object; span=(34, 42), match='TXN12345'> when i use search in place of findall the output will be like this