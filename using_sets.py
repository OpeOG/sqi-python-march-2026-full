#***********************************SETS *********************************

# The order of items in a set is not guaranteed as it is UNORDERED COLLECTION
numbers = {32, 5, 2, 3, 6, 9, 8}
print(numbers)

# Duplicates are not allowed in a SET. It eradicates duplicate since it will not throw an error
numbers = {32, 5, 2, 3, 6, 9, 8, 5}
print(numbers)

# You can't INDEX or SLICE  a SET
# numbers = {"one", "two", "three", "four", "eight", "five"}
# print(numbers[0]) # this will throw an error -------> is not suscriptable

# Creating an empty set
unique_laptops = set() # you don't make use of {} to create an empty set because python will see it as a dictionary
print(unique_laptops)
print(type(unique_laptops))

# A set can hold data of multiple types at once
randoms = {"A townhall... different", 2009, 106.5, None, False, 0, 1} # In sets, python sees 0 as boolean False so it will take just one, (either false or ), same goes to True and 1, it takes either True or 1
print(randoms)


martials_arts = {"kungfu", "karate", "tai chi", "wing chun", "jeet-kun-do", "muay tay"}
# Finding the length of a set
print(len(martials_arts))

# Finding the datatype of the martials_arts
print(type(martials_arts)) # to find the data type

# Finding a specific item in the set
print("wing chun" in martials_arts)

indian_movies = ["baahubali", "players", "hebbulli", "mard", "dhoom", "dhoom", "players", "my name is khan"]

# This removes duplicate items  from the indian_movies in an UNORDERED format
unique_movies = list(set(indian_movies))
print(unique_movies)

# This removes duplicate items  from the indian_movies in an ORDERED format
unique_ordered_movies = list(dict.fromkeys(indian_movies).keys())
print(unique_ordered_movies)

# ***************************SETS METHODS*******************************
# add method
phones = set()
# The .add method on a set allows us to add items to our set (order is not guaranteed)
# You can't save this to a variable just like '.append()'
phones.add("Samsung")
phones.add("Huawei")
phones.add("Redmi")
phones.add("iPhone")
phones.add("Motorolla")
phones.add("Nokia")
print(phones)


# To clear a set, we use the .clear()
# phones.clear()
# print(phones)


# Creating a copy of a set
phones_copy = phones.copy()
print(phones_copy)



new_phones = {'T-mobile', 'Techno', 'Motorola', 'Lenovo', 'Infinix', 'Alcatel', 'Sagem', 'Nokia'}
# Find the items that phones have that the new_phones set does not have
print(phones.difference(new_phones))

# Find and return only the items that are common to both sets
print(phones.intersection(new_phones))

# Creating a full collection of all phones and new_phones
print(phones.union(new_phones))


# The symetric difference, it means give what are unique to both sets, which means check the two. In other words, what are the things both of them do not have in common.
print(new_phones.symmetric_difference(phones))

# Remove an item from a set
new_phones.remove("Sagem") # this will thrown an error if not found in the set"keyerror"
print(new_phones)

new_phones.discard("Sagem") # this will not throw  an error  if not found unlike "remove"

# Removing a random item from the set. If you have a specific item you want to remove, make use of discard or remove
print(new_phones.pop())


# Using the update() method on a set
print(phones)
print(new_phones)

new_phones.update(phones)
print(new_phones)

more_phones = ['microsoft', 'asus' ]
new_phones.update(more_phones)
print(new_phones)

values = {'red', 'green', 'blue'}
new_color = 'yellow'
values.add(new_color) # we make use of "add" here since it's not a collection, it's just a string, but when it's a collection you make use of "update"
print(values)

animals = {'cat', 'dog', 'rabbit'}
extra_items = ['horse', 'sheep']
animals.update(extra_items)
print(animals)