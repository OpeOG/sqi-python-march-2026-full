# QUESTION 1: Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
# the set and print the result.
fruits = {"air", "water", "food"}
valid_if_food_is_in_set = "water" in fruits
print(valid_if_food_is_in_set)
# OR
print('water' in fruits)

# QUESTION 2: Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" 
# to the set and print the updated set.
colors = {"red", "green", "blue"}
new_color = "yellow"
colors.add(new_color)
print(colors)

# QUESTION 3: Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.
animals = {"cat", "dog", "rabbit"}
new_animals = ["horse", "sheep"]
animals.update(new_animals)
print(animals)

# QUESTION 4:  Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.
countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)


# QUESTION 5: Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")
print(cities)


# QUESTION 6: Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
conversion_to_set = set(seasons)
print(conversion_to_set)

# QUESTION 7: Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# QUESTION 8: Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
print(setA.intersection(setB))   # What are common to both sides

# QUESTION 9:  Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)

# QUESTION 10:  Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)

# QUESTION 11: Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)

# QUESTION 12: Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
letters = {"a", "b", "c"}
second_letters = {"b", "c", "d"}
print(letters.difference(second_letters))  

print(letters.symmetric_difference(second_letters))


# QUESTION 13 : Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# 	Add the items from another set {"Amazon", "Facebook"} and print the updated set tech_brands without creating a new set.
tech_brands = {"Apple", "Google", "Microsoft"}
new_set = {"Amazon", "Facebook"}
tech_brands.update(new_set)
print(tech_brands)

# QUESTION 14 : Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
# 	remove method to remove "Charlie" from the set and print the updated set. Then try to 
# 	remove "Eve" from the set and observe the behavior.
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
print(students)
# students.remove("Eve")
print(students)  # KeyError: 'Eve'


#  QUESTION 15: Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
# 	duplicates and print the resulting set.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
print(set(numbers_list))

# QUESTION 16: 	Given a string text = "hello", convert this string to a set to find the unique 
# 	characters and print the resulting set.
text = "hello"
print(set(text))

# unique_ordered_movies = list(dict.fromkeys(indian_movies).keys()) This not the question nor the answer but read on it tonight

#  17. 	Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
# 	many items are in the set and print the result.
vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))

#  18. 	Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
# 	number of items in the set.
gadgets = {"laptop", "smartphone","tablet", "smartwatch"}
print(len(gadgets))
