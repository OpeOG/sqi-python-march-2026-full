# QUESTION 1: Create a list called fruits with items "apple", "banana", and "orange". Print the first item.

# fruits = ["apple", "banana", "orange"]
# first_item = fruits[0]
# print(first_item)

# QUESTION 2: Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing

# colors = ["red", "green", "blue"]
# last_item = colors[-1]
# print(last_item)

# QUESTION 3: Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7 (inclusive of index 3, exlusive of 8)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers [3:8])
# or range(1, 11)
# then list(range(1, 11)). Use range to generate numbers

# QUESTION 4: Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.

# alphabets = ["a", "b", "c", ..., "z"]
# or alphabets = list('abcdefghijklmnopqrstuvwxyz')
# print(alphabets[-3:])
# or making use of modules, import string
# alphabets = list(string.ascii_lowercase)
# print(alphabets[-3:])

# QUESTION 5: Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.

# ages = [20, 30, 40]
# ages [1] = 35
# print(ages)

# QUESTION 6: Create a list called cities with items "New York", "London", "Paris", Insert "Tokyo", at the beginning of the list.

# cities = ["New York", "London", "Paris",]
# cities.insert(0, "Tokyo")
# print(cities)

# QUESTION 7: Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.

# fruits = ["apple", "banana", "cherry"]
# list_of_items = len(fruits)
# print(list_of_items)

# QUESTION 8: Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.

# items_prices = [10.5, 20.0, 15.75]
# print(type(items_prices))

# QUESTION 9: Create a list called mixed with items 10, "apple", True. Print the list.
# items_mixture = [10, "apple", True]
# print(items_mixture)

# QUESTION 10: Create a list called books with items "Python", "Java". Append "Javascript" to the end of the list.
# books = ["Python", "Java"]
# books.append("Javascript")
# print(books)

# QUESTION 11: Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1
# items = ["Alice", "Bob", "Eve"]
# items.insert(1, "Charlie")
# print(items)

# QUESTION 12: Create a list called list1 and list2 with items 1,2,3 and ,4,5,6 respectively. Extend list1 with list2
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)

# QUESTION 13: Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
# students = ["Alice", "Bob"]
# new_students = ("Charlie", "David")
# students.extend(new_students)
# print(students)

# QUESTION 14: Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# colors = ["red", "green", "blue"]
# colors.remove("green")
# print(colors)

# QUESTION 15: Create a list called numbers with items 10, 20, 30, 40. Use del keyword to remove the item at index 2.
# list_of_numbers = [10, 20, 30, 40]
# del list_of_numbers[2]
# print(list_of_numbers)

# QUESTION 16: Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)