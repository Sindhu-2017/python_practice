#A=P(1+r/n)t
principle=0
rate=0
time=0
while True:
    principle=int(input("Enter the principle amount:"))
    if principle<0:
        print("Principle cant be less than or equal to zero")
    else:
        break

while True:
    rate=int(input("Enter the rate amount:"))
    if rate<0:
        print("rate cant be less than or equal to zero")
    else:
        break

while True:
    time=int(input("Enter the time amount:"))
    if time<0:
        print("time cant be less than or equal to zero")
    else:
        break

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s : {total:.2f}")