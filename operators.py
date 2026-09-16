#arithmetic
a = 25
b = 4
print("Addition =",a+b)
print("Subtraction =",a-b)
print("Multiplication =",a*b)
print("Division =",a/b)
print("Remainder =",a%b)


#comparison
a = 10
b = 20
if a==b:
  print("A is equals to b")
if a!=b:
  print("A is not equals to b")
if a<b:
  print("a is less than b")
if a>b:
  print("a is less than b")


#odd or even
number=int(input("Enter the number to check odd or even ?:"))
if number%2 ==0:
  print("Even")
else:
  print("Odd")


#positive ,negative,zero
number=int(input("Enter the number to check odd or even ?:"))
if number>0:
  print("Positive")
elif number<0:
  print("Negative")
else:
  print("Zero")


#test pass or fail
expected_username = "admin"
expected_password = "admin123"
username=input("Enter the username :")
password=input("Enter the password :")
if username == expected_username and password == expected_password :
  print("Test pass")
else:
  print("Test fail")

#marks
mark=int(input("Enter the mark ?:"))
if mark<0 or mark>100:
  print("Invalid mark")
elif mark >=90:
  print("Grade A")
elif mark>=75:
  print("Grade B")
elif mark>=50:
  print("Grade C")
elif mark>=35:
  print("Grade D")
else:
  print("Fail")

#QA Challenge
expected_status_code = 200
actual_status_code = 200

if expected_status_code == actual_status_code:
  print("API TEST PASS")
else:
  print("API TEST FAIL")