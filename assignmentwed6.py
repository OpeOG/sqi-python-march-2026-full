# QUESTION 1: Exercise: Notes & Notebook System

# A simple note-taking app allows users to organize their thoughts.

# Each note has:

# a title
# a content/body text

# The notebook stores multiple notes and should provide useful functionality.

# Sample Execution
# note1 = Note("Shopping List", "eggs milk bread butter")
# note2 = Note("Ideas", "build an app write a book")
# note3 = Note("Reminder", "call mom tomorrow")

# notebook = Notebook([note1, note2, note3])

# print(notebook.total_words())
# print(notebook.find_by_keyword("app"))

# Expected Output
# 12
# Ideas
# class Note:
#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.content = content
# class Notebook:
#     def __init__(self, notes: list[Note]):
#         self.notes = notes

#     def total_words(self):
#         return sum(len(note.content.split()) for note in self.notes)
    
#     def find_by_keyword(self, keyword):
#         for note in self.notes:
#             if keyword in note.content:
#                 return note.title
#         return "No matching note found"
# note1 = Note("Shopping List", "eggs milk bread butter")
# note2 = Note("Ideas", "build an app write a book")
# note3 = Note("Reminder", "call mom tomorrow")

# notebook = Notebook([note1, note2, note3])

# print(notebook.total_words())
# print(notebook.find_by_keyword("app"))

# # QUESTION 2:Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.

# class Line:
#     def __init__(self, coor1, coor2): 
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (y2 - y1) / (x2- x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinate1, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6

# QUESTION 3: Fill in the class
# import math

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume (self):
#         return math.pi * (self.radius ** 2) * self.height

#     def surface_area(self):
#         return (2 * math.pi * self.radius ** 2) + (2 * math.pi * self.radius * self.height)

# # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2

# QUESTION 4: Scenario: You want to create a bank account that supports deposits and withdrawals.

# Task: Create a bank account class that has two attributes:

# owner
# balance

# and two methods:
# deposit
# Withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values for the amounts into 
# the methods directly, no need for loops either.

# class Account:
#     def __init__(self, owner: str, balance: float):
#         self.owner = owner
#         self.balance = balance
#     def __str__(self):
#         return f"Account owner: {self.owner}, Balance: {self.balance}"
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}")
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New balance is {self.balance}")
#         else:
#             print("Insufficient funds")
# acct1 = Account("Nelson", 100)
# print(acct1)
# # print(acct1.owner)
# # print(acct1.balance)
# acct1.deposit(50)
# acct1.withdraw(30)
# acct1.withdraw(100)
# acct1.withdraw(50)