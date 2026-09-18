# Q1
class Employee:
    # Q4
    company="ABC"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Q2
    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        print("Company :",self.company)



emp=Employee("Sindhuja",23000)
emp2=Employee("Kavya",20000) 
emp.display()
emp2.display()

# Q3
# self.name =>is the instance variable which belongs to object
# name => its a formal parameter receives from object creation place



# Q5
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        # Q6
        super().speak()
        print("Bark")

dog=Dog()
dog.speak()

# Q7
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

calc=Calculator()
print(calc.add(10,20))

# Q8
# instance method-Its belongs to object and it receives self
# class method-it belongs to class and it receives cls 
# static method-its dont need either self or cls and uses @staticmethod

# Q9
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car")

class Bike(Vehicle):
    def start(self):
        print("Bike")

vehicle=[Car(),Bike()]
for v in vehicle:
    v.start()


# Q10
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance =",self.balance)

    def withdraw(self,amount):
        if amount >self.balance:
            print("Amount exceeded")
        else:
            self.balance=self.balance-amount
            print("Balance =",self.balance)

    def display_balance(self):
        print("Balance =",self.balance)

bank=BankAccount("Sindhuja",2000)
bank.deposit(1200)
bank.withdraw(2000)
bank.deposit(1000)
bank.display_balance()



        