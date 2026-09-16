#Print numbers from 1 to 20 using a for loop.

for i in range(1,21):
  print(i)


#Print only even numbers from 1 to 20.
for i in range(1,21):
  if i%2 ==0:
    print(i)

#Print the multiplication table of 5:

for i in range(1,11):
  print(5,"*",i,"=",i*5)


#Using a while loop, print:

i=10
while i>0:
  print(i)
  i=i-1

#Print numbers from 1 to 10, but stop when the number reaches 6 using break.
i=1
while i<=10:
  if i==6:
    break
  print(i)
  i=i+1

#Print numbers from 1 to 10 but skip 5 using continue.
i=0
while i<10:
  i=i+1
  if i==5:
    continue
  print(i)
  
#Q7
results = ["PASS", "PASS", "FAIL", "PASS", "FAIL"]
for i in range(5):
  print("Test case ",i+1,":",results[i])
  
#multiplication table
table=int(input("Which multiplication table you want ?:"))
for i in range(1,11):
  print(table,"*",i,"=",table*i)
