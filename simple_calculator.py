# Project Overview:
# Create a simple calculator program that performs basic arithmetic operations in a file 
# named `simple_calculator.py`. 
# Objective: Build a calculator that can perform addition, subtraction, multiplication, and division operations on two numbers.

# Calculator Operations:
# Addition (+): Adds two numbers.
# Subtraction (-): Subtracts the second number from the first.
# Multiplication (*): Multiplies two numbers.
# Division (/): Divides the first number by the second (handling division by zero).

# User Interface:
# - Display a menu with options for each operation.
# - Prompt the user to enter two numbers and select an operation.
# - Perform the selected operation and display the result.
# - Handle division by zero scenarios.
# - Assume the user enters only valid data type inputs.

# Example Program Execution:
# Welcome to the Simple Calculator
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit

# Enter your choice from 1 to 5: 3
# Enter first number: 3
# Enter second number: 4

# 3.0 X 4.0 = 12.0

# Welcome to the Simple Calculator
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice from 1 to 5: 5


# Functions to Implement:
# addition(num1, num2): Performs addition of two numbers.
# subtraction(num1, num2): Performs subtraction of two numbers.
# multiplication(num1, num2): Performs multiplication of two numbers.
# division(num1, num2): Performs division of two numbers, handling division by zero.


def addition(num1, num2):
    print(f"{num1} + {num2} = {num1+num2}")

def subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1-num2}")

def multiplication(num1, num2):
    print(f"{num1} X {num2} = {num1*num2}")

def division(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return
    print(f"{num1} / {num2} = {num1/num2}")




print("Welcome to the Simple Calculator")
menu = """
Select operation:
add -  Addition
sub -  Subtraction
mul -  Multiplication
div -  Division
quit - Exit
"""


while True:
    print(menu)
    choice = input("Enter your choice from the menu above: ")

    if choice == "quit":
        print("goodbye👋")
        break

    if choice not in ["add", "sub", "mul", "div"]:
        print("Invalid operation")
        continue
#  ctrl d, shift ctrl, right arrow - test the shortkeys to see their function
    
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

    if choice == "add":
        addition(first_num, second_num)
    elif choice == "sub":
        subtraction(first_num, second_num)
    elif choice == "mul":
        multiplication(first_num, second_num)
    elif choice == "div":
        division(first_num, second_num)
