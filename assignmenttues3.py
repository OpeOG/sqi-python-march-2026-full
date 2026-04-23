# QUESTION 1: Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
dimensions = (10, 20, 30)
length, width, height = dimensions
print(length, width, height)

# QUESTION 2: Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(y)

# QUESTION 3: Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
person = ("John", 25, "Engineer")
name, age, profession = person
print(profession)

# QUESTION 4: Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1_, student_2), subjects, age = data
print(student_2)

# OR ------------->
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1_, student_2), *_ = data

# QUESTION 5: Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
colors = ("red", "green", "blue", "yellow")
color1, color2, color3, color4 = colors
print(color1, color2)

# OR 
colors = ("red", "green", "blue", "yellow")
color1, color2, *_ = color2
print(color1, color2)


# QUESTION 6: Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, position), (dept1, dept2) = record
print(age, dept1)

# QUESTION 7: Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
triplet = ("one", "two", "three")
first_value, second_value, third_value = triplet

# OR 
_, second_value, _ = triplet
print(second_value)

# QUESTION 8: Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_ID, (category, price), (year) = info
#OR
product_ID, (category, price), (dd, mm, yy) = info  # Since we only need the 'year'
print(product_ID, category, price, year )

# QUESTION 9: Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
first_tuple, second_tuple, (third1, third2) = nested_tuple
print(third2)

# QUESTION 10: Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
first_fruit, (second_fruit, quantity), third_fruit = inventory
# OR
(fruit1, qty1), (fruit2, qty2), (fruit3, qty3) = inventory
print(quantity)
