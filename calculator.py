#python calculator
operator=input("Enter an operator (+ - * /) :")
num1 =int(input("Enter the first number :"))
num2 =int(input("Enter the second number :"))

if operator == '+':
  print(f"Addition :{num1+num2}")
elif operator == "-":
  print(f"Subtraction :{num1-num2}")
elif operator == "*":
  print(f"Multiplication :{num1*num2}")
elif operator == "/":
  print(f"Division :{round(num1/num2,2)}")
else:
  print("Invalid operator")



