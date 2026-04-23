#  ctrl d, shift ctrl, right arrow - test the shortkeys to see their function

# print("***************** USER INFORMATION ***********")
# print("FIRSTNAME: Opeyemi")
# print("LASTNAME: Ogunboye")
# print("EMAIL: nelsonogunboye@gmail.com")

# print("For more information, call 09034255276")

#  Write your code below
# print("Hello world!")
# print("Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# print("Knead the dough for 10 minutes.")
# print("Add 3g of Salt.")
# print("Leave to rise for 2 hours.")
# print("Bake at 200 degrees C for 30 minutes.")

# String Manipulation
# (/n) -----> Breaking to a new line 
# print("Hello World!\n Hello World!")

# Cocatenation-----> Combination of diff. strings
# print("Hello" + " " + "Nelson")

# Input
# input("Hello Nelson!")

#Python Variables
# name = "Nelson"
# print("name")

# finding the length of a string
# name = "Nelson"
# print(len(name))

# print("Hello,\n World!")
# text = ("Python is amazing!")
# print(text[2:10:2])

# first_name = "Opeyemi"
# last_name = "Ogunboye"
# school_of_institution = "Olabisi Onabanjo University"
# Using f-string method
# print(f"My name is first name is {first_name} and my last name is {last_name} and i studied at {school_of_institution}")
# Using format method
# print('{} is {} years old, {} feet tall, and it is {} that she is a student.'.format(first_name, last_name, school_of_institution,))
# print(f' My first name is {} and my {} and i attend {}.'.format(first_name, last_name, school_of_institution))

# text = "hello, my name is Peter, I am 26 years old"
# x = text.split(", ")
# states = ("Lagos", "Ibadan", "Kogi", "Abia")
# seperator = "/"
# result = seperator.join(states)
# print(result)
# words = ['Hello', 'World', 'Python']
# sentence = ''.join(words)
# print(sentence)


# QUICK WORK  ON DICTIONARY

# QUESTION 1: Access and print the name of the teacher of "class2".
school = {
    "class1": {
        "students": ["Alice", "Bob"],
        "teacher": "Mr. Smith"
    },
    "class2": {
        "students": ["Charlie", "David"],
        "teacher": "Ms. Johnson"
    }
}
print(school["class2"]["teacher"])


# QUESTION 2: Access and print the second employee in the "Engineering" department.
company = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"]
}
print(company['Engineering'][1])


# QUESTION 3: Access and print the name of the second assistant.
university = {
    "faculty": {
        "professors": ["Dr. Smith", "Dr. Brown"],
        "assistants": ["Ms. Green", "Mr. White"]
    },
    "students": ["John", "Jane", "Alice", "Bob"]
}
print(university["faculty"]["assistants"][1])

# QUESTION 4:  Access and print the price of the third fruit.
store = {
    "fruits": [
        {"name": "apple", "price": 0.5},
        {"name": "banana", "price": 0.2},
        {"name": "cherry", "price": 1.5}
    ],
    "vegetables": [
        {"name": "carrot", "price": 0.3},
        {"name": "lettuce", "price": 1.0},
        {"name": "onion", "price": 0.4}
    ]
}
price_of_third_fruit = store["fruits"][2]["price"]
name_of_third_fruit = store['fruits'][2]['name']
print(f"The price of {name_of_third_fruit} is ${price_of_third_fruit}")


# QUESTION 5 : 	Access and print the second non-fiction book.
library = {
    "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
    "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
}
print(library['non-fiction'][2])

# QUESTION 6: 	Access and print the age of the first child.
family = {
    "parents": ["John", "Jane"],
    "children": [
        {"name": "Tom", "age": 5},
        {"name": "Lucy", "age": 8}
    ]
}
age_of_firstchild = family["children"][1]["age"]
name_of_firstchild = family["children"][1]["name"]
print(f"This is the family of Tokunbo's, and they have two children, the second child's name is {name_of_firstchild} and he's {age_of_firstchild}yrs old.")

# QUESTION 7:  Access and print the name of the second main course.
restaurant = {
    "menu": {
        "appetizers": ["soup", "salad"],
        "main_courses": ["steak", "pasta"],
        "desserts": ["cake", "ice cream"]
    },
    "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
}
print(restaurant['menu']['main_courses'][1])

# QUESTION 8: 	Access and print the department of the user of the first desk.
workspace = {
    "desks": [
        {"user": "Alice", "department": "HR"},
        {"user": "Bob", "department": "Engineering"}
    ],
    "equipment": {"computers": 20, "printers": 10}
}
print(workspace['desks'][0]['department'])

# QUESTION 9: Access and print the name of the second designer.
team = {
    "developers": ["Dev A", "Dev B"],
    "designers": ["Designer X", "Designer Y"],
    "projects": ["Project 1", "Project 2"]
}
print(team['designers'][1])

# QUESTION 10: Access and print the second international destination.
travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
{"flights": 1500, "hotels": 2000}}
print(travel['international'][1])

# Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
student = {
    'name' : "John",
    'age' : 20,
    'grade' : "A"
}
print(student['name'])

# Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
product = {
    'name' : "Laptop",
    'price' : 999.99,
    'stock' : 50
}
product["price"] = 899.99
print(product)

# Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
employee = {
    'name' : "Alice",
    'position' : "Manager"
}
employee['salary'] = 50000
print(employee)

# Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
inventory = {
    'apple' : 10,
    'banana' : 5,
    'orange' : 8
}
del inventory["banana"]
print(inventory)

# Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
person = {
    'name' : "Bob",
    'age' : 25,
    'city' : "New York"
}
copied_version = person.copy()
person['state'] = "Lagos"
copied_version = person.copy()
print(person)
print(copied_version)  # How do i go about it if i don't want it to affect the original key "person". Ask your instructor


# Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
grades = {
    'math' : "A",
    'science' : "B",
    'history' : "C"
}
print(list(grades.keys()))

#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.

#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
game = {
    'title' : "Minecraft",
    'genre' : "Sandbox",
    'rating' : 4.5
}
print(list(game.items()))


# Q1. Given this dictionary, change the "math" score to 95.
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# student["scores"]["math"] = 95
# print(student)


#  Q2. Add a new subject "science" with score 90 inside "scores".
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
student["scores"]["science"] = 90
print(student)

# Q3. Change the author's name of "Python 101" to "Mike".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Python 101"]['author'] = "Mike"
print(library)

#  Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Data Science"]['publisher'] = "O'Reilly"
print(library)

#  Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Alice"]['work'] = "555-999"
print(contacts)

#  Q6. Change Bob’s "home" number to "555-000".
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Bob"]["home"] = "555-000"
print(contacts)
#  Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
 # into the list of students.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# students [1] = "Eve", "scores": {"math": 88, "english": 92}
# print(students)   #ASK CHATGPT FOR GUIDANCE

# Q8 Change Bob's english score from 70 to 78.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# student[1]["scores"]["english"] = 78  #ASK CHATGPT

# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# # inside Alice’s record under a new key "enrollment".
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 78}}
# ]
# Q10. In this shop cart, add a new product "Notebook" with price 200.
# cart = {
#     "items": [
#         {"name": "Pen", "price": 10},
#         {"name": "Book", "price": 50}
#     ],
#     "owner": "Alice"
# }





