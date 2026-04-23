# OOP - Object Oriented Programming -----> It is a way of writing Python code by organizing things into objects.
# Class ----> A class is the  blueprint, example: car, student, laptop, employee, 
# Object ----> An object is an actual item created from a class (blueprint). So if Car is a class, Toyota Camry can be one object and Honda Civic can be another object.
# Attributes ----> Attributes are the data and variables that belongs to an object. So for a car, atributes can be, brand, year, model, color
# Methods -----> Methods are functions inside a class.They describe what an object can do.
# For a Car, methods can be:
# start_engine()
# stop_engine()
# car_info()

# Things to take note
# def __init__(self, brand, model):
# This is a special method called the constructor.
# self.brand becomes "Toyota"
# self.model becomes "Corolla"
# So self helps each object keep its own data.

# """The 4 major ideas in OOP
# 1. Encapsulation -----> This means keeping data and methods together inside one class.
# For example, in Laptop:
# data: brand, ram, storage
# methods: laptop_info(), upgrade_ram()
# 2. Inheritance -----> This means one class can take features from another class.
# 3. Polymorphism ----> It means the same method name can work in different ways for different classes.
# 4. Abstraction ------> This means hiding unnecessary details and showing only what is important.""""
# paradigm - a way of programming

# structural, modular, oop, functional


# oop => classes and objects and methods


# capital or upper camel casing

# BankAccount bank_account bankAccount
# snake_casing ----> my_name, student_score, total_price
# camelCasing ---> myName, studentScore, totalPrice
# PascalCasing ---> MyName, StudentScore, TotalPrice
# kebab-casing ----> student-score, total-price, # sqi-python-mar-2026

# class ClassExample:
#     pass


# class Person:  this means you're telling Python to create a blueprint for person(persons)
# def __init__(self, first_name: str, last_name: str, age: int, height: float, is_dark: bool, is_male: bool):
#         print("__init__ running")
#         self.person_first_name = first_name
#         self.person_last_name = last_name
#         self.age = age
#         self.height = height
#         self.is_dark = is_dark
#         self.is_male = is_male

    
#     def walk(self):
#         print("I am walking")

#     def introduce_oneself(self):
#         gender = "male" if self.is_male else "female"
#         print(f"My name is {self.person_first_name} {self.person_last_name}. I am {gender}. I am {self.age} years old")

#     def say_mood(self, mood, time_of_day):
#         print(f"I am {mood} {time_of_day}.")



# # objects
# ope = Person("Ope", "Nelson", 39, 1.78, False, True)
# winnie = Person("Winifred", "Igboama", 24, 1.56, True, False)

# # encapsulation

# print(ope.age)
# winnie.walk()
# ope.introduce_oneself()
# print(ope.person_first_name)
# winnie.say_mood("happy", "today")



# Create a class called BankAccount with the attributes bank_name, account_holder, is_savings, account_balance
# A BankAccount has the methods `deposit`, `withdraw`, `account_details`

# class BankAccount:
#     """This is a bank account class that helps to withdraw and deposit money"""
#     def __init__(self, bank_name: str, account_holder: str, is_savings: bool, account_balance: float):
#         self.bank_name = bank_name
#         self.account_owner = account_holder
#         self.account_balance = account_balance
#         self.has_above_50000 = account_balance > 50000
#         self.account_type = "SAVINGS" if is_savings else "CURRENT"

#     def account_details(self):
#         return f"""
# Account Owner: {self.account_owner}
# Account Balance: {self.account_balance}
# Account Type: {self.account_type}
# # """

#     def deposit(self, amount: float):
#         self.account_balance += amount
#         return "Deposit successful"

#     def withdraw(self, amount: float):
#         if amount > self.account_balance:
#             return "Insufficient funds"
#         self.account_balance -= amount
#         return "Withdrawal successful"


# account_one = BankAccount("Opay", "Winifred Igboama", True, 9000.54)
# account_two = BankAccount("First Bank", "Ope Nelson", False, 900_000_000.08)

# # print(account_one.account_balance)
# # account_one.account_balance = 7655.67
# # print(account_one.account_balance)

# print(account_one.account_details())
# print(account_one.deposit(5678))
# print(account_one.account_details())


# print(account_two.account_details())
# print(account_two.withdraw(5400.56))
# print(account_two.account_details())



# ***********************************QUICK WORK ***************************************************
# 1. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.
# class Car:
#     def __init__(self, brand, model, year, horsepower, fuel_type):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type

#     def car_info(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}."


# car1 = Car("Toyota", "Camry", 2022, 203, "petrol")
# car2 = Car("Tesla", "Model 3", 2023, 283, "electric")
# car3 = Car("Lexus", "RX 350", 2021, 450, "petrol")

# print(car1.car_info())
# print(car2.car_info())
# print(car3.car_info())


# 2. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.
# class Student:
#     def __init__(self, name: str, age: int, grades: int):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     def average_grade(self):
#         average = sum(self.grades) / len(self.grades)
#         return average
#     def is_passing(self):
#         if self.average_grade() >= 50:
#             return True
#         return False
# student1 = Student("Ope", "90", [20, 30, 50, 45])
# student2 = Student("Winnie", "45", [35, 40, 80, 55])
# print(student1.average_grade())
# print(student2.average_grade())

# print(student1.is_passing())
# print(student2.is_passing())

# class Circle:
#     PI = 22 / 7

#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2

#     def area(self):
#         # return self.PI * (self.radius ** 2)
#         return Circle.PI * (self.radius ** 2)
    
#     def circumference(self):
#         # return 2 * self.PI * self.radius
#         return 2 * Circle.PI * self.radius
    

# circle = Circle(6)
# print(circle.area())

# print(circle.PI)

# print(Circle.PI)



# class Circle:
#     PI = 22 / 7

#     def __init__(something, radius):
#         something.radius = radius
#         something.diameter = radius * 2

#     def area(anything):
#         # return anything.PI * (anything.radius ** 2)
#         return Circle.PI * (anything.radius ** 2)
    
#     def circumference(sonmething_else):
#         # return 2 * sonmething_else.PI * sonmething_else.radius
#         return 2 * Circle.PI * sonmething_else.radius
    



# circle = Circle(6)
# print(circle.area())


# 1. Create a class called Laptop with the following attributes:
#    - brand
#    - ram (in GB)
#    - storage (in GB)
#    - price
#
#    The class should have two methods:
#    - upgrade_ram(extra_ram): increases the ram by extra_ram
#    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and {storage}GB storage costs {price}."
#
#    After defining the class, create 2 different Laptop objects with different values.
# class Laptop:
#     def __init__(self, brand: str, ram: int, storage: int, price: float):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

#     def upgrade_ram(self, extra_ram):
#         self.ram += extra_ram
#     def laptop_info(self):
#         return f"{self.brand} laptop with {self.ram}GB RAM and {self.storage}GB storage costs {self.price}."
#   # fn and f2 to change at once  
# laptop1 = Laptop("HP", 16, 256, 550_000.00, )
# laptop2 = Laptop("Macbook", 16, 256, 100_000.00, )

# print(laptop1.laptop_info())
# print(laptop2.laptop_info())
# laptop2.upgrade_ram(32)
# print(laptop2.laptop_info())


# 2. Create a class called Employee with the following attributes:
#    - name
#    - position
#    - salary
#
#    The class should have two methods:
#    - give_raise(amount): increases salary by amount
#    - employee_info(): returns "{name} works as a {position} and earns {salary} per year."
#
#    After defining the class, create 3 different Employee objects with different values.

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def give_raise(self, amount):
#         self.salary += amount

#     def employee_info(self):
#         return f"{self.name} works as a {self.position} and earns {self.salary} per year."


# employee1 = Employee("Ope", "Student", 45000)
# employee2 = Employee("Winnie", "Python Web Developer", 60000)
# employee3 = Employee("Tobi", "Python Web Developer", 75000)

# print(employee1.employee_info())
# print(employee2.employee_info())
# print(employee3.employee_info())

# ***********************************QUICK WORK ***************************************************

# ************************************** ASSIGNMENT**************************************************
# 3. Create a class called Phone with the following attributes:
#    - brand
#    - model
#    - battery_percentage
#
#    The class should have two methods:
#    - charge(amount): increases battery_percentage by amount (do not exceed 100)
#    - phone_status(): returns "{brand} {model} battery is at {battery_percentage}%."
#
#    After defining the class, create 2 different Phone objects with different values.
# class Phone:
#     def __init__(self, brand: str, model: str, battery_percentage: int):
#         self.brand = brand
#         self.model = model
#         if battery_percentage > 100:
#             self.battery_percentage = 100
#         else:
#             self.battery_percentage = battery_percentage
#     def charge(self, amount):
#         self.battery_percentage += amount
#         if self.battery_percentage > 100:
#             self.battery_percentage = 100
#     def phone_status(self):
#         return f"{self.brand} {self.model} battery is at {self.battery_percentage}"
# phone1 = Phone("iPhone", 2024, 40)
# phone2 = Phone("Samsung", 2024, 80)
# phone1.charge(40)
# print(phone1.phone_status())

# phone2.charge(35)
# print(phone2.phone_status())

# 4. Create a class called Product with the following attributes:
#    - name
#    - price
#    - quantity_in_stock
#
#    The class should have three methods:
#    - restock(amount): increases quantity_in_stock by amount
#    - sell(amount): decreases quantity_in_stock by amount
#    - inventory_value(): returns total value of stock (price * quantity_in_stock)
#
#    After defining the class, create 3 different Product objects with different values.
# class Product:
#     def __init__(self, name: str, price: float, quantity_in_stock: int):
#         self.name = name
#         self.price = price
#         self.quantity_in_stock = quantity_in_stock
#     def restock(self, amount): 
#         self.quantity_in_stock += amount
#     def sell(self, amount):
#         if amount <= self.quantity_in_stock:
#             self.quantity_in_stock -= amount
#         else:
#             print("Not enough stock available.")
#     def inventory_value(self):
#         return self.price * self.quantity_in_stock
# product1 = Product("Generator", 700_000.00, 10)
# product2 = Product("AC", 1_500_000.00, 25)
# product3 = Product("Television", 750_000.00, 40)
# (product1.restock(10))
# (product2.restock(15))
# (product3.restock(20))

# (product1.sell(10))
# (product2.sell(20))
# (product3.sell(18))

# print(product1.inventory_value())
# print(product2.inventory_value())
# print(product3.inventory_value())

# 5. Create a class called Course with the following attributes:
#    - course_name
#    - instructor
#    - students (a list of student names)
#
#    The class should have two methods:
#    - add_student(name): adds a student to the students list
#    - total_students(): returns the number of students enrolled
#
#    After defining the class, create 2 different Course objects with different values.
# class Course:
#     def __init__(self, course_name: str, instructor: str, students: list):
#         self.course_name = course_name
#         self.instructor = instructor
#         self.students = students
#     def add_student(self, *names):
#         self.students.extend(names)
#     def total_students(self):
#         return len(self.students)
# course1 = Course("Data Science", "Winnifred", ["Opeyemi", "Dele"])
# course2 = Course("Javascript", "Wisdom", ["Oreoluwa", "Debby"])
# course1.add_student("Kole", "Samuel")
# print(course1.total_students())

# course2.add_student("Wande")
# print(course2.total_students())

# 6. Create a class called Circle with the following attributes:
#     - radius
#
#     The class should have two methods:
#     - area(): returns 3.14 * radius * radius
#     - circumference(): returns 2 * 3.14 * radius
#
#     After defining the class, create 3 different Circle objects with different values.
# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius
# circle1 = Circle(3.5)
# print(circle1.area())
# print(circle1.circumference())

# circle2 = Circle(7.5)
# print(circle2.area())
# print(circle2.circumference())

# circle3 = Circle(10.8)
# print(circle3.area())
# print(circle3.circumference())
# ************************************** ASSIGNMENT**************************************************
#*****************************QUICK WORK**********************************************
# Create a class called OnlineCourse

# Attributes:

# course_name
# instructor
# students (this should be a list)

# Methods:

# enroll_student(student_name): adds a student to the list
# remove_student(student_name): removes student if they exist
# total_students(): returns number of students
# course_info():
# returns:
# "{course_name} by {instructor} has {number_of_students} students enrolled."

# Task:

# Create 2 different OnlineCourse objects
# Add and remove students
# Display course details

# Sample execution
# course1 = OnlineCourse("Python Basics", "Mr. A")
# course2 = OnlineCourse("Web Development", "Ms. B")

# course1.enroll_student("Alice")
# course1.enroll_student("Bob")

# course2.enroll_student("Charlie")
# course2.enroll_student("Dave")
# course2.remove_student("Charlie")

# print(course1.course_info())
# print(course2.course_info())

# Expected Output
# Python Basics by Mr. A has 2 students enrolled.
# Web Development by Ms. B has 1 students enrolled.
# class OnlineCourse:
#     def __init__(self, course_name, instructor):
#         self.course_name = course_name
#         self.instructor = instructor
#         self.students = []

#     def enroll_student(self, student_name):
#         self.students.append(student_name)

#     def remove_student(self, student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)

#     def total_students(self):
#         return len(self.students)

#     def course_info(self):
#         return f"{self.course_name} by {self.instructor} has {self.total_students()} students enrolled."


# course1 = OnlineCourse("Python Basics", "Mr. A")
# course2 = OnlineCourse("Web Development", "Ms. B")

# course1.enroll_student("Alice")
# course1.enroll_student("Bob")

# course2.enroll_student("Charlie")
# course2.enroll_student("Dave")

# course2.remove_student("Charlie")

# print(course1.course_info())
# print(course2.course_info())
# #*****************************QUICK WORK**********************************************
# class Book:
#     def _init_(self, author: str, title: str, no_of_pages: int, is_fiction: bool, year_of_pub: int):
#         self.author = author
#         self.title = title
#         self.no_of_pages = no_of_pages
#         self.is_fiction = is_fiction
#         self.year_of_pub = year_of_pub



# class Library:
#     def _init_(self, books: list[Book]):
#         self.books = books

#     def add_book(self, book: Book):
#         self.books.append(book)

#     def how_many_pages(self):
#         return sum(book.no_of_pages for book in self.books)


# book1 = Book(author="George Orwell", title="1984", no_of_pages=328, is_fiction=True, year_of_pub=1949)
# book2 = Book(author="Michelle Obama", title="Becoming", no_of_pages=448, is_fiction=False, year_of_pub=2018)
# book3 = Book(author="J.K. Rowling", title="Harry Potter and the Philosopher's Stone", no_of_pages=223, is_fiction=True, year_of_pub=1997)

# print(book1)
# print(book2)
# print(book3)

# community_library = Library([book1, book2])
# community_library.add_book(book3)
# print(community_library.books)  # 
# print(community_library.how_many_pages())


# A CartItem is made up of item, price and qty
# A Cart is made up of a list of CartItems
# A Cart can return its total
# class CartItem:
#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity

# class Cart:
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.price * item.quantity for item in self.items)
# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200

# Movie Ticket Booking System

# A cinema is building a simple system to calculate the total cost of tickets purchased by a customer.

# Each ticket type has:

# a movie name
# a price per ticket
# a number of tickets purchased

# The system should compute the total cost for all tickets in a booking.

# Sample Execution
# ticket1 = Ticket("Avengers", 3500, 3)
# ticket2 = Ticket("Lion King", 2500, 2)

# booking = Booking([ticket1, ticket2])
# print(booking.total_cost())

# Expected Output
# 15500
# class Ticket:
#     def __init__(self, movie_name: str, price_per_ticket: float, num_of_tickets: int):
#         self.movie_name = movie_name
#         self.price_per_ticket = price_per_ticket
#         self.num_of_tickets = num_of_tickets

# class Booking:
#     def __init__(self, tickets: list[Ticket] ):
#         self.tickets = tickets

#     def total_cost(self):
#         return sum(ticket.price_per_ticket * ticket.num_of_tickets for ticket in self.tickets)
# ticket1 = Ticket("Avengers", 3500, 3)
# ticket2 = Ticket("Lion King", 2500, 2)

# booking = Booking([ticket1, ticket2])
# print(booking.total_cost())
# #*****************************QUICK WORK**********************************************

 # -------------INSTANCE ATTRIBUTES OUTSIDE __INIT__----------------

# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")
 
#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.my_total
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item = CartItem("eggs", 250, 4)
# cart_item.total()
# cart_item.display_cart()

# # -------------INSTANCE ATTRIBUTES OUTSIDE __INIT__----------------
# Difference between __str__ and __repr__
# __str__ → nice for users
# __repr__ → more formal, useful for developers/debugging

# Very simple way to remember:

# str() = readable -----> print(obj) or str(obj)
# repr() = detailed -----> repr(obj)
# __len__ for len(obj)

# -------------MAGIC DUNDER METHODS----------------
# magic double-underscore method
# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")

#     def __str__(self):
#         return f"CartItem has {self.item} that costs {self.price} -> {self.total()}"
    
#     def __repr__(self):
#         return f'CartItem(item="{self.item}", price={self.price}, quantity={self.quantity})'

#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.price * self.quantity
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item1 = CartItem("eggs", 250, 4)

# print(cart_item1)

# print(str(cart_item1))

# cart_item2 = CartItem("bread", 450, 10)
# print(cart_item2)

# print(repr(cart_item1))
# print(repr(cart_item2))

# cart = Cart([cart_item1, cart_item2])
# cart = Cart([cart_item1, cart_item2, cart_item1, cart_item2])

# print(len(cart))

# -------------MAGIC DUNDER METHODS----------------


# isinstance() asks:

# “Is this object made from this class/type?”
# ------------------------------------ISINSTANCE()------------------------------------------------

# num = 10
# print(isinstance(num, int))
# print(isinstance(num, bool))


# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")

#     # def __str__(self):
#     #     return f"CartItem has {self.item} that costs {self.price} -> {self.total()}"
    
#     def __repr__(self):
#         return f'CartItem(item="{self.item}", price={self.price}, quantity={self.quantity})'

#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.price * self.quantity
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item1 = CartItem("eggs", 250, 4)

# # print(cart_item1)

# # print(str(cart_item1))

# cart_item2 = CartItem("bread", 450, 10)
# # print(cart_item2)

# # print(repr(cart_item1))
# # print(repr(cart_item2))

# cart = Cart([cart_item1, cart_item2])
# cart = Cart([cart_item1, cart_item2, cart_item1, cart_item2])

# print(isinstance(cart, Cart))
# print(isinstance(cart, CartItem))



# ------------------------------------ISINSTANCE()------------------------------------------------


#  ctrl d, shift ctrl, right arrow - test the shortkeys to see their function
# ENCAPSULATION
# INHERITANCE
# POLYMORPHISM

#*****************************************INHERITANCE*************************************
# class Animal:
#     def __init__(self, name: str, type: str, has_wings: bool, has_tail: bool, is_mammal: bool, sound: str):
#         self.name = name
#         self.type = type
#         self.has_wings = has_wings
#         self.has_tail = has_tail
#         self.is_mammal = is_mammal
#         self.sound = sound

#     def introduce_yourself(self):
#         # ternary operator
#         return f"I am a/an {self.type}. My name is {self.name}. It is {self.has_wings} that I have wings. I {self.sound}."
        


# fido = Animal("Fido", "cat", False, True, True, "meow")
# print(fido.introduce_yourself())

# # MRO - Method Resolution Order

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, type, False, True, True, "bark")
#         self.breed = breed

#     def introduce_yourself(self):
#         animal_intro = super().introduce_yourself()
#         return animal_intro + f" I am a/an {self.breed}."
    
#     def bark(self):
#         return "I am barking"

# jaguar = Dog("Jaguar", "German Sherpherd")
# print(jaguar.introduce_yourself())
# print(jaguar.sound)
# print(jaguar.name)
# print(jaguar.bark())


# Exercise: Digital Library System

# You are modeling a simple system for a digital library.

# 🎯 What is expected
# There should be a base class representing a general library item.
# The class should store basic information such as:
# title
# creator (e.g., author, director, etc.)
# whether it is available
# The class should include a method that describes the item in a sentence.
# There should be a child class that represents a specific type of item (e.g., a Book).
# This child class should:
# Extend the base class
# Add at least one extra property (e.g., number of pages, genre, etc.)
# Modify the description method to include the extra detail
# There should be another child class representing a different type of item (e.g., Movie or Magazine).
# This class should:
# Also inherit from the base class
# Have its own unique attribute
# Provide its own version of the description
# Demonstrate:
# Creating objects from each class
# Accessing attributes
# Calling methods
# How inheritance changes behavior


# ▶️ Example Execution
# book1 = Book("1984", "George Orwell", True, 328)
# print(book1.describe())

# movie1 = Movie("Inception", "Christopher Nolan", False, 148)
# print(movie1.describe())

# print(book1.title)
# print(movie1.is_available)

# ✅ Expected Output (example)
# This item is titled 1984 by George Orwell. It is available. It has 328 pages.
# This item is titled Inception by Christopher Nolan. It is not available. Duration is 148 minutes.
# 1984
# False

# class LibraryItem:
#     def __init__(self, title: str, creator: str, is_available: bool):
#         self.title = title
#         self.creator = creator
#         self.is_available = is_available
#     def describe(self):
#         return f"This item is titled {self.title} by {self.creator} is {self.is_available} that is available"
    
# class Book(LibraryItem):
#     def __init__(self, title: str, creator: str, is_available: bool, pages: int):
#         super().__init__(title, creator, is_available)
#         self.pages = pages
#     def describe(self):
#         return f"This item is tiled {self.title} by {self.creator} is {self.is_available} that is available. It has {self.pages} pages"
# class Movie(LibraryItem):
#     def __init__(self, title: str, creator: str, is_available: bool, duration: float):
#         super().__init__(title, creator, is_available)
#         self.duration = duration
#     def describe(self):
#         return f"This item is tiled {self.title} by {self.creator} is {self.is_available} that is available. Duration is {self.duration}"
# book1 = Book("1984", "George Orwell", True, 328)
# print(book1.describe())

# movie1 = Movie("Inception", "Christopher Nolan", False, 148)
# print(movie1.describe())

# print(book1.title)
# print(movie1.is_available)
#*****************************************INHERITANCE*************************************

# -----------------------------------------------POLYMPORPHISM------------------------------------------------------

# morphine, muffin, morphing

# class Device:
#     def operate(self):
#         print("Operating device")

# class SmartPhone:
#     def operate(self):
#         print("Operating Smartphone")

# class AirConditioner:
#     def operate(self):
#         print("Operating Air Conditioner")

    
# device = Device()
# smartphone = SmartPhone()
# ac = AirConditioner()

# devices = [device, smartphone, ac]

# for device in devices:
#     device.operate()


# class Device:
#     def operate(self):
#         print("Operating device")

# class SmartPhone(Device):
#     pass

# class AirConditioner(Device):
#     pass

    
# device = Device()
# smartphone = SmartPhone()
# ac = AirConditioner()

# devices = [device, smartphone, ac]

# for device in devices:
#     device.operate()




# --------------------------------INHERITANCE EXAMPLE-------------------------------------

# FANTASY GAME


# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.


# class GameCharacter:
#     def __init__(self, name: str, health: int, attack_power: int):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, target: GameCharacter):
#         if self == target:
#             print(f"{self.name} cannot attack themself")
#             return

#         target.health -= self.attack_power
#         print(f"{self.name} attacks {target.name}!")
#         print(f"{target.name}'s health is now {target.health}")



# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.


# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

# 3. Handle cases where the target is the same as the attacker.


# class Warrior(GameCharacter):
#     def __init__(self, name, health, attack_power, armor):
#         super().__init__(name, health, attack_power)
#         self.armor = armor

#     def attack(self, target):
#         target.health -= 10
#         super().attack(target)
    

# class Mage(GameCharacter):
#     def __init__(self, name, health, attack_power, mana):
#         super().__init__(name, health, attack_power)
#         self.mana = mana

#     def attack(self, target):
#         if self.mana < 5:  # guard
#             print("not enough mana to attack")
#             return
#         super().attack(target)
#         self.mana -= 5


# # SAMPLE EXECUTION 1
# warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
# mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
# warrior.attack(mage)
# # Output:
# # Thor attacks Merlin!
# # Merlin's health is now 80
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 90
# mage.attack(warrior)
# # Output:
# # Merlin attacks Thor!
# # Thor's health is now 80
# mage.attack(warrior)
# # Output:
# # Not enough mana to attack
# print(warrior.health)  # 80
# print(mage.health)  # 80
# print(mage.mana)  # 0


# # SAMPLE EXECUTION 2
# merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
# gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 80
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 90
# gaius.attack(gaius)
# # Output:
# # Gaius cannot attack themself
# gaius.attack(merlin)
# # Output:
# # Gaius attacks Merlin
# # Merlin’s health is now 80
# merlin.attack(gaius)
# # Output:
# # Merlin attacks Gaius
# # Gaius’s health is now 60
# merlin.attack(gaius)
# # Output:
# # Not enough mana to attack

# ******************************************* ASSIGNMENT *****************************************************
# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.


# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)

# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# 3. Handle negative refuel amounts.
# SAMPLE  EXECUTION
# Create objects


class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel
    def launch(self):
        if self.fuel < 50:
            print("Not enough fuel")
        else:
            print(f"Launching {self.name}")
            self.fuel -= 50
    def refuel(self, amount):
        if amount < 0:
            print("Cannot refuel with negative amount.")
        else:
            self.fuel += amount
            print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}")

class CargoShip(Spacecraft):
    def __init__(self, name: str, fuel: int, cargo_weight: int):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight
    def launch(self):
        fuel_needed = 50 + (self.cargo_weight * 2)
        if self.fuel < fuel_needed:
            print("Not enough fuel to launch")
        else:
            print(f"Launching {self.name} with cargo!")
            self.fuel -= fuel_needed
class PassengerShip(Spacecraft):
    def __init__(self, name: str, fuel: int, passenger_count: int):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count
    def launch(self):
        if self.passenger_count > 100:
            print ("Too many passengers. Cannot launch.")
        elif self.fuel < 50:
            print("Not enough fuel to launch")
        else:
            print(f"Launching {self.name}")
            self.fuel -= 50
 
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)

# Attempt to launch both ships
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 200 - (50 + 30*2) = 90

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 100 - 50 = 50

# Refuel both ships
cargo_ship.refuel(50)
# Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

passenger_ship.refuel(30)
# Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# Launch again after refueling
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 140 - (50 + 30*2) = 30

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 80 - 50 = 30

# Try to refuel with invalid amount
cargo_ship.refuel(-10)
# Output: Cannot refuel with negative amount.

# Test PassengerShip with too many passengers
passenger_ship.passenger_count = 120
passenger_ship.launch()
# Output: Too many passengers. Cannot launch.

# Try to launch cargo ship with low fuel
cargo_ship.launch()
# Output: Not enough fuel to launch.
# ******************************************* ASSIGNMENT *****************************************************

# --------------------------------INHERITANCE EXAMPLE-------------------------------------

        