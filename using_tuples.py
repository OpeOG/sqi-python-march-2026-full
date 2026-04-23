# # () -----> tuple with four items
# actors = ('Kevin Hart', 'Dwayne Johnson', 'James Bond', 'Chadwick Boseman',)
# print(actors)

# # Creating an empty tuple
# actors = ()
# #or
# actors = tuple()
# print(actors)
# print('Actors tuple: ')

# # Creating a tuple with only one item
# universites = ('OOU',)
# print(universites)

# # Finding out the length of a tuple
# universites = ('UI', "OOU", "OAU", "Unilag", "LASU", "Uniport", "Uniabuja")
# uni_length = len(universites)
# print(f"There are {uni_length} universities in our collection")

# # Creating a tuple with duplicate items 
# universites = ('UI', "OOU", "OAU", "Unilag", "LASU", "Uniport", "Uniabuja", "OOU", "OAU")
# print(universites)

# # Creating a tuple without the parentheses 
# universites = 'UI', "OOU", "OAU", "Unilag", "LASU", "Uniport", "Uniabuja"
# print(universites)

# # Tuple immutability  --------> You can't add to the items unlike lists
# universites = 'UI', "OOU", "OAU", "Unilag", "LASU", "Uniport", "Uniabuja"
# universites[1] = 'Babcock'
# print(universites)

# # Modifying items in a tuple by typecasting to a list
# universites = 'UI', "OOU", "OAU", "Unilag", "LASU", "Uniport", "Uniabuja"
# universites = list(universites)
# universites.append('SQI')
# universites.append('Unizik')
# print(universites)
# universites = tuple(universites)
# print(universites)

# # Tuple with mixed data types
# data = True, True, "Johnson", "Maverick", 30 > 4, 18, 106.5
# print(data)

# collection_types = "Hashmap"
# print(collection_types)

# Note: sorted() function used on a tuple gives back a LIST. So if you want it to give you a tuple, you'll have to typecast it to a tuple.
# fav_fruits = ('apple', 'banana', 'cherry', 'avocado', 'pawpaw', 'breadfruit', 'grape', 'pineapple')
# print((sorted(fav_fruits))) # this will give us a list
# print(tuple(sorted(fav_fruits))) # this will give us a tuple

# fav_fruits = ('apple', 'banana', 'cherry', 'avocado', 'pawpaw', 'breadfruit', 'grape', 'pineapple')
# # # 1
# fruits_count = len(fav_fruits)
# print(fruits_count)

# # # 2
# fav_fruits = list(fav_fruits)
# print(fav_fruits)
# fav_fruits.remove('grape')
# fav_fruits.remove('pineapple')
# print(fav_fruits)

# fav_fruits = tuple(fav_fruits)
# print(fav_fruits)

# # 3
# sorted_descending_format = sorted(reversed=True)
# print(sorted_descending_format)

# #4.
# fav_fruits = list(fav_fruits)
# most_favorite_fruit = fav_fruits.append('strawberry')
# fav_fruits = tuple(fav_fruits)
# print(fav_fruits)

# # #5.
# fav_fruits = list(fav_fruits)
# del fav_fruits[-1]
# del fav_fruits[-1]
# fav_fruits = tuple(fav_fruits)
# print(fav_fruits)


# Finding out whether an item can be found in a tuple
# programming_languages = "R", "C++", "Rust", "Golang", "Drat", "Javascript"
# print("R" in programming_languages)

# fast_programming_languages =  "C++", "C#", "Rust", "Golang", "Java", "C"

# user_response = input('Enter programming langauge: ')

# valid = user_response in fast_programming_languages

# print(f"It is {valid} that the {user_response} is a fast programming language")

# # Creating a single tuple of data from multiple tuples
# tuple1 = ("rabbit", "hare", "horse")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# long_tuple = tuple1 + tuple2 + tuple3
# print(long_tuple)

# # Replicating the items in a tuple
# colors = 'red', 'green', 'blue'
# print(colors * 10)

# Write the question later 
# item1 = input('Enter an household item: ')
# item2 = input('Enter an household item: ')
# item3 = input('Enter an household item: ')

# household_items_collection = item1, item2, item3
# print(household_items_collection)

# Tuple methods (count, index)
# countries = 'Nigeria', 'Ghana', "Belgium", 'Netherlands', 'USA', 'UK', 'Nigeria', 'Ghana'
# nigeria_count = countries.count('Nigeria')
# print(nigeria_count)

# Or just do it straightforward this way

# print(countries.count('Nigeria'))

# First position of Ghana in our countries tuple
# print(countries.index('Ghana'))

# Count the number of "uk" irrespective of the case
# countries = 'Nigeria', 'Ghana', "Belgium", 'Netherlands', 'USA', 'UK', 'Nigeria', 'Ghana', 'uk', 'Belize', 'China', 'Burundi'
# print(len(countries)) # you can't use length on a tuple so you have to change it to a tuple then use your "len" function. So you can confirm it to a string first then use "len"
# print(str(countries)).lower()
# print(countries.count('uk'))
# ---------------> This is throwing an error so make sure to ask chat for what's wrong when your're connected to the internet

# #or -----> If you don't want it to look like a tuple. Use this;
# countries = ' '.join(countries).lower()
# print(countries.count('uk'))


# Unpacking a tuple --------> Tuple unpacking
# instructors = ('Ms Winnie', 'Mr. Tobi', 'Ms Sekinat', 'Mr Paul', 'Mr Wisdom', 'Mr. Dotun',)
# winnie, tobi, seki, paul, wisdom, dotun = instructors
# print(seki)
# print(wisdom)

# Extracting only the first two items from the tuple.
# winnie, tobi, *others = instructors
# print(winnie)
# print(tobi)
# print(others)  # this will give you your value in a list[]

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *others) = fruits # Pyhton will assign the remaining items to the last variable which is (others)
# (green, *yellow, others) = fruits #  Python will assign values
# to the variable (yellow) until the number of values left matches the number of variables left
# print(green)
# print(yellow)
# print(others)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *_ ) = fruits
# print(*_)

# Unpacking only the first and last instructor
# winnie, *_, dotun= instructors
# print(winnie)
# print(*_)

# winnie, tobi, *_ = instructors  # This means the variable(*_) has no value, it's not needed.
# print(tobi)

# firstname, lastname, opeyemi, dele = ("Oluwatobi", "Dada", ("Opeyemi", "Nelson"), ("Dele", "Oludayo"))
# print(firstname)
# print(lastname)
# print(opeyemi)
# print(dele)

# firstname, lastname, (ope_fname, ope_lname), (dele_fname, dele_lname) = ("Oluwatobi", "Dada", ("Opeyemi", "Nelson"), ("Dele", "Oludayo"))
# print(ope_fname, ope_lname)

# record = ("Jane", (32, "Manager", ["HR, "Finance]))
# name, (age, position), (dept1, dept2) = record

# coordinates = (1.5, 2.5, 3.5)
# coord1, coord2, coord3 = coordinates


# Swap the values of coordinate 1 to ccoordinate2 and coordinate3....Just swap the values
# coord1, coord2, coord3 = coordinates
# coord1, coord2, coord3 = coord2, coord3, coord1
# print(coord1, coord2, coord3)

# When you slice a tuple, you get a tuple in return
# countries = 'Nigeria', 'Ghana', "Belgium", 'Netherlands', 'USA', 'UK', 'Nigeria', 'Ghana'
# countries = countries[-1:]

# countries = 'Nigeria', 'Ghana', "Belgium", 'Netherlands', 'USA', 'UK', 'Nigeria', 'Ghana'
# countries = countries[-1] + countries[-2] + ''.join(countries[:3])

# Turning a string to a tuple
# string = "Madagascar"
# tuple_of_string = tuple(string)
# print(tuple_of_string)

# students = [('Tobi, 20'), ('John, 30'), ('Bowen, 30'), ('Johnny, 40')]
# print(students)

# students.append(('Wyaat, '))
# print(students)

# # students = [['Tobi, 20'], ['John, 30'], ['Bowen, 30'], ['Johnny, 40']]
# # students[0] = ["Johnson, 30"]  # this will throw because we are now on a tuple

# # but this will work
# students = [['Tobi, 20'], ['John, 30'], ['Bowen, 30'], ['Johnny, 40']]
# students[0][0] = "Button" # This is replacing the first item of the first list of our tuple

# students[0].append('Baller')
# print(students)

# # Deleting an item that is directly an item of a tuple will throw an error e.g
# del students[0] # so it's either you clear the whole tuple or you start indexing till you reach the part where you can delete.


# item = ("bag", "television", "refrigerator" )
# item_y = list(item)
# item_y[0] = "phone"
# item = tuple(item_y)
# print(item)


 
