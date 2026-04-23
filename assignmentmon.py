# QUESTION 1: Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically
list_of_names = ["Zoe", "Alice", "Bob"]
list_of_names.sort()
print(list_of_names)

# QUESTION 2: Create a list called ages with items 25, 35, 20. Sort the list in descending order
ages = [25, 35, 20]
ages.sort(reverse=True)
print(ages)

# QUESTION 3: Sorting lists is CASE-SENSITIVE by default. Create a list called words with items "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
words = ["Apple", "banana", "Orange"]
words.sort(key=str.lower)
print(words)

# QUESTION 4: Create a list called called numbers with items 1, 2, 3, 4. Print the list in reverse order.
list_of_numbers = [1, 2, 3, 4]
list_of_numbers.reverse()
print(list_of_numbers)

# QUESTION 5: Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing.
list_of_items = ["a", "b", "c", "d"]
reversed_order = list_of_items[::-1]
print(reversed_order)

# QUESTION 6: Create a list called original with items "one", "two", "three". Create a copy of the list.
original_items = ["one", "two", "three"]
print(original_items.copy())

# QUESTION 7: Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
list1 = ["a", "b"]
list2 = ["c", "d"]
list1.extend(list2)
print(list1)

# QUESTION 8: Access and print the second subject of the first person in the list.

data = [
    ["Alice", 25, ["Math", "Physics"]],
    ["Bob", 30, ["Chemistry", "Biology"]],
    ["Charlie", 35, ["History", "Geography"]]
]
print(data[0][2][1])

# QUESTION 9: Access and print the first value in the list of numbers associated with "San Francisco".
records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]
print(records[1][1][0])

# QUESTION 10: Get the first e in Ayo's gender and Get Ben's age.
group = [
    ["Ayo", ["Female", 12]],
    ["Ben", ["Male", 9]]
]
print(group[0][1][0][1])
print(group[1][1][1])

# QUESTION 10: Get the I in Nina's gender and Get Tobi's age
records = [
    ["Tobi", ["Male", [6]]],
    ["Nina", ["Female", [7]]]
]
print(records[1][0][1])
print(records[0][1][1])

# QUESTION 11: Get the two oo's in X1's 2nd mobility status (loose) together (slicing) and get the battery percentage of R2
robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", [["joint", "loose"], "error"]]
]
print(robot_grid[2][1][0][1][1:3])
print(robot_grid[0][1][1])

# QUESTION 12: Get the Five in the Jazz song title and get the duration of the Jazz song. Also find out how many words make up the title of the second jazz song
playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Jazz", ["Take The A Train", 10.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][1][0][-4:])
duration_of_jazz_song = playlist[0][1][1]
print(f"The duration of jazz song is {duration_of_jazz_song}")
title_of_second_jazz_song = playlist[1][1][0]
total_words_of_title_of_second_jazz_song =(playlist[1][1][0]).split()
print(total_words_of_title_of_second_jazz_song)

# QUESTION 13: Get the letter v in Tiger's category and get the first letter of the Frog's type
animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
print(animals[1][1][0][5])
print(animals[2][1][0][0])