import os

class Arith: #Class For All Arithmatic Operations
    def add(self , x, y):
        return x + y

    def subtract(self ,x, y):
        return x - y

    def multiply(self ,x, y):
        return x * y

    def divide(self ,x, y): #
        try:
            return x / y
        except:
            return "Cannot divide by zero"

s=Arith()

def get_user_input():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    return num1, operator, num2

while True:
    os.system('cls')
    
    num1, operator, num2 = get_user_input()
    
    os.system('cls')
    
    if operator == '+':
        result = s.add(num1, num2)
    elif operator == '-':
        result = s.subtract(num1, num2)
    elif operator == '*':
        result = s.multiply(num1, num2)
    elif operator == '/':
        result = s.divide(num1, num2)
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        continue
    
    os.system('cls')
    print("Result: ", result," \n " , " \n ")
    
    
    another_calculation=input("Another Calculation : ? \n Yes ? or No ? ").lower()
    if another_calculation != 'yes':
        break