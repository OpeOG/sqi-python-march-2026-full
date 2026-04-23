#************************THE LIST DATA TYPE********************************
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and mutable. Allows duplicate members.
# students = ["Tobi", "John", "Milly", "Dele"]
# print(students)
# Accessing items from list using Indexing
# print(students[0])
# print(students[0] + students[-1])
# Note: A list is an ORDERED Collection
# Replacing an item in a list
# favorite_cities = ["Paris", "New York", "Ohio", "Illinois"]
# favorite_cities[1] = "Geneva"
# favorite_cities[-1] = "Minnesota"
# print(favorite_cities)

# Allow the user to see these lists of favorite_cities and then select the index and what they want to replace that favorite city
# favorites_cities = ["Paris", "New York", "New Jersey", "Ohio", "Illinois"]
# print(favorites_cities)

# length_of_cities = len(favorites_cities)
# index = int(input(f'Enter an index (between 0-{length_of_cities}): '))
# new_city_name = input(f'Enter a new name for city at index{index }: ')
# favorites_cities[index] = new_city_name
# print(favorites_cities)


# footballers_names = ["Messi", "Boniface", "Ronaldo", "Suarez", "Pogba"]
# print(footballers_names)
# length_of_footballers = len(footballers_names)
# index = int(input(f'Enter an index (between 0-{length_of_footballers}): '))
# new_footballer_names = input(f'Enter a new name for footballer at index{index}: ')
# footballers_names[index] = new_footballer_names
# print(footballers_names)


# Deleting an item from a list
# footballers_names = ["Messi", "Boniface", "Ronaldo", "Suarez", "Pogba"]
# del footballers_names #This deletes the whole footballer_names
# del footballers_names[1]
# # this deletes at index 1
# print(footballers_names)

# Duplicates in a list
# footballers_names = ["Messi", "Boniface", "Ronaldo", "Suarez", "Pogba", "Boniface", "Ronaldo", "Messi", "Suarez"]
# print(footballers_names)

# A list can hold data of multiple types
# data = ["tobi", 21, "lagos", True, 106.5, 106.5]
# print(data)
# print(data[1] + 1)

#Creating an empty list
# best_nigerian_presidents = []
#or 
# best_nigerian_presidents = list()
# print(best_nigerian_presidents)


# *************************List Methods**************************
# ***************************************************************

# foods = ["Bread", "Beans"]
# 'append'- Adding something( or an item) into a list. The item can be of any data type... AT THE END OF THE LIST e.g
# foods.append("Rice")
# foods.append("Porridge")
# foods.append("Eba")
# print(foods)

#'clear'removes all items in your list
# foods.clear()
# print(foods)
# # or 
# foods = []
# print(foods)

#'count' tells us how many times a particular item can be found in the list,
# cars = ["Rolls Royce", "Bentley", "Masseratti", "Porsche", "Bentley", "Bentley"]
# print(cars.count("Bentley"))  #Counts how many Bentley exists in the list
# print(cars[-2].count('t'))  #

# 'extend' #It takes a tuple or list of items and adds them at the end of our lists.
# ai_tools = ["Chatgpt", "Grok", "Claude", "MetaAI", "MidJourney"]
# new_ai_tools = ('SnapAI', 'WordHero', 'Sora')

# ai_tools.extend(new_ai_tools)
# print(ai_tools)

# 'insert' #allows us to add an item into the list while specifying exactly where the items should be placed
# ai_tools = ["Chatgpt", "Grok", "Claude", "MetaAI", "MidJourney"]
# ai_tools.insert(1, 'NewAgeAI')
# ai_tools.insert(-1, 'SnapAI')
# print(ai_tools)

#Llama3
# Copilot
# ai_tools.insert(0, 'Copilot')
# ai_tools.insert(0, 'Llama3')
# print(ai_tools)

# or 
# ai_tools.insert(0, 'Llama3')
# ai_tools.insert(1, 'Copilot')
# print(ai_tools)

# 'remove' removes an item from the list using that item's exact value. Throws error if item does not exist
# ai_tools = ["Chatgpt", "Grok", "Claude", "MetaAI", "MidJourney"]
# ai_tools.remove('Claude')
# print(ai_tools)

# 'pop' -> removal from a list and allowing us to store that removed value into a variable  or do something else with that removed value
# Note: it removed the last item of the list if not specified
# ai_tools = ["Chatgpt", "Grok", "Claude", "MetaAI", "MidJourney"]
# removed_item = ai_tools.pop()
# ai_tools.pop()
# print(ai_tools)
# print("The removed item is: ", removed_item)

# 'copy' --> 
# laptops = ["HP", "Dell", "Lenovo", "Mac", "Toshiba", "Samsung"]
# laptop_copy = laptops.copy()  #Shallow copy: use this when you want to disconnect copy
# laptop_copy = laptops
# laptops.append("Alienware")
# print(laptop_copy)

#'index' ---->
# laptops = ["HP", "Dell", "Lenovo", "Mac", "Toshiba", "Samsung"]
# print(laptops.index('Dell'))

# 'reverse' -----> takes a list and reverse it
# movies = ["Prison Break", "Blacklist", "Ozark", "Money Heist", "Breaking Bad", "Dexter"]
# movies.reverse() #This will affect the order of the list
# print(movies)

# Reverse without affecting the order of our original list
# movies_reversed = movies[::-1]
# print(movies_reversed)
# print(movies)

# #or 
# movies_reversed = reversed(movies)
# print(list(movies_reversed))

# A mirror of all the movies
# print(movies + movies[::-1])

# 'sort'-------> It's used to arrange items in a list in ascending or descending order. It works for data of the same type.

# movies = ["Prison Break", "Blacklist", "Ozark", "Money Heist", "Breaking Bad", "Dexter"]
# movies.sort() #Ascending order
# or movies.sort(reverse=False) #Still ascending order but it's unnecessary to do it this way
# print(movies)

# movies.sort(reverse=True)  #Descending order


# If you don't want it to affect the original variables
# sorted_movies = sorted(movies)
# print(sorted_movies)

# movies = ["Prison Break", "Blacklist", "vikings", "you", "his or hers", "beauty in black" "Ozark", "Money Heist", "Breaking Bad", "Dexter"]
# movies.sort()  # it will sort the lowercase at the end. ASCII code - Google about it
# If you dont't want this, make use of something like this:
# movies.sort(key=str.lower)

# Sort this list in descending order, irrespective of the case of each movie
# movies = ["Prison Break", "Blacklist", "vikings", "you", "his or hers", "beauty in black" "Ozark", "Money Heist", "Breaking Bad", "Dexter"]
# movies.sort(reverse=True, key=str.lower)

# If you don't want to update the previous list itself
# sorted_in_desc_movies = sorted(movies, key=str.lower, reverse=True)
# print(sorted_in_desc_movies)
# print(movies)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix) # It will give us everything
# print(matrix[0][1]) # this will give us "2" at the first index which index zero [0]

# Getting multiple items from the the matrix
# print(matrix[-1][0] * matrix[0][0] * 3)

# Access the number 105 in the matrix below:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, [42, 4, [48, 105]], 9]
# ]
# print(matrix[-1][1][2][1])

# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]
# summing the numbers 10, 20, 30
# print(sum(nested_list[0][0]))

# Replicate the alice in our nested list number of times we have the last score in the scores list.
# alice = nested_list[0][0]
# num_of_times = nested_list[1][0]
# print( alice * num_of_times)

# Replicate the Bob in our nested list number of times we have the last score in the scores list.
# bob = nested_list[0][1]
# num_of_times = nested_list[1][1]
# print(Bob * num_of_times)



# Get the two 00's in X1's 2nd mobility status (loose) together (slicing) and get the battery percentage of R2
robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", [["joint", "loose"], "error"]]
]
print(robot_grid[2][1][0][1][1:3])
print(robot_grid[0][1][1])
# Get the Five in the Jazz song title and Get the duration of the Jazz song title and get the duration of the Jazz song. Also find out how many words make up the title of the second jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Jazz", ["Take The A Train", 10.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
# print(playlist[0][1][0][-4:])
# duration_of_playlist = playlist[0][1][1]
# print(f"The duration of the jazz song is: {duration_of_playlist}")


# Tuple is a collection which is ordered and immutable. Allows duplicate members.
# Set is a collection which is unordered, mutable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and mutable. No duplicate members.




# print("**************************WEDDING GUEST MANAGER**************************")

#Stage 1
confirmed_guests = ["Alloe", "Charlie", "Eve", "Bob", "Frank", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print(confirmed_guests)
print(waitlist)

# Stage 2
waitlist.append("Ken")
waitlist.append("Joak")
waitlist.append("Ivy")

print(confirmed_guests)
print(waitlist)

# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")

print(confirmed_guests)
print(waitlist)

# Stage 4
confirmed_guests.remove("Alloe")
confirmed_guests.append(waitlist.pop(0))


print(confirmed_guests)
print(waitlist)

# Stage 5
charlie_found = "Charlie"  in confirmed_guests
print(f" It is {charlie_found} that Charlie is in confirmed guests")
print(confirmed_guests)
print(waitlist)

# Stage 6 
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")

print(confirmed_guests)
print(waitlist)

# Stage 7
# print("Stage 7")
confirmed_guests.append(waitlist.pop(0))
confirmed_guests.append(waitlist.pop(0))
print(confirmed_guests)
print(waitlist)

# Stage 8
# print("Stage 8")
waitlist.remove("Oliver")

print(confirmed_guests)
print(waitlist)

# Stage 9
# print("Stage 9")
last_3_guests = confirmed_guests[-3:]
print(f"The last three guests are: {last_3_guests}")

print(last_3_guests)
print(waitlist)

# Stage 10
# print("Stage 10")
confirmed_guests.append(waitlist.pop(0))
print(confirmed_guests)
print(waitlist)

# Stage 11
# print("Stage 11")
num_of_confirmed_guests = len(confirmed_guests)
print(f"Total number of guests: {num_of_confirmed_guests}")
print(confirmed_guests)
print(waitlist)

# Stage 12
# print("Stage 12")
confirmed_guests_sorted = sorted(confirmed_guests)
print(confirmed_guests)
print(f"Sorted version of guests: {confirmed_guests_sorted}")
print(waitlist)

#Stage 13
# print("Stage 13")
# confirmed_guests.remove("Grace")
confirmed_guests.remove("Noah")
confirmed_guests.append("Collins")

#Stage 14
# print("Stage 14")
guests_list_for_caterer = confirmed_guests.copy()
print(f"Guest list copy for caterer = {guests_list_for_caterer}")
print(confirmed_guests)
print(waitlist)

# Stage 15
waitlist.clear()