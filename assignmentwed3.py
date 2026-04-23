# QUESTION 1: Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
students = ["John", 20, "A"]
students = {
    'name' : "John",
    'age' : 20,
    'grade' : "A"
}
print(students['name'])

# QUESTION 2: Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
products = ["Laptop", 999.99, 50]
products = {
    'name' : "Laptop",
    'price' : 999.99,
    'stock' : 50
}
products['price'] = 899.99
print(products['price'])

# QUESTION 3: Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
employee = ["Alice", "Manager"]
employee = {
    'name' : "Alice",
    'position' : "Manager"
}
employee['salary'] = 50000
print(employee)

# QUESTION 4: Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
inventory = {
    'apple' : 10,
    'banana' : 5,
    'orange' : 8
} 
del (inventory['banana'])
print(inventory)

#OR

# removed_inventory = inventory.pop('banana')
# print(inventory)
# print(removed_inventory)

# QUESTION 5: Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
person = {
    'name' : "Bob",
    'age' : 25,
    'city' : "New York"
}
person_copy = person.copy()
print(person_copy)

# QUESTION 6: Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
family = {
    'child1' : {
        'name' : "Bob",
        'age' : 15
    },
    'child2' : {
        'name' : "Alice",
        'age' : 17
    },
    'child3' : {
        'name' : "Anita",
        'age' : 19
    }
}
age1 = (family['child2']['age'])
age2 = (family['child1']['age'])
print(age1 + age2)

# QUESTION 7: Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
car = {
    'brand' : "Toyota",
    'model' : "Corolla",
    'year' : "2020"
}
print(car['model'])

# QUESTION 8: Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings = {
    'volume' : 50,
    'brightness' : 75,
    'language' : "English"
}
settings['language'] = "Spanish"
print(settings)

# QUESTION 9: Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
scores = {
    'maths' : 90,
    'science' : 85,
    'english' : 88
}
scores.pop('science')
print(scores)

# QUESTION 10: Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
menu = {
    'starter' : "Soup",
    'main_course' : "Steak",
    'dessert' : "Ice Cream"
}
print('appetizer' in menu.keys())

# QUESTION 11: Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
config = {
    'theme' : "dark",
    'language' : "English",
    'timezone' : "UTC"
}
print(config.clear())

# QUESTION 12: Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
phone_book = {
    'Alice' : 23454387609,
    'Bob' : 2349034255289,
    'Charlie' : 2349034255280
}
print(phone_book.items())

# QUESTION 13: Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
grades = {
    'math' : "A",
    'science' : "B",
    'history' :"C"
}
print(list(grades.keys()))

# QUESTION 14: Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
employee = {
    'name' : "David",
    'position' : "Engineer",
    'salary' : 70000
}
print(list(employee.values()))

# QUESTION 15: 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
game = {
    'title' : "Minecraft",
    'genre' : "Sandbox",
    'rating' : 4.5
}
print(list(game.items()))
