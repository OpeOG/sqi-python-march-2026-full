# While loop
# For loop
# | Situation                        | Best loop |
# | -------------------------------- | --------- |
# | Go through letters in a word     | `for`     |
# | Go through numbers 1 to 20       | `for`     |
# | Keep asking until user says stop | `while`   |
# | Repeat while number is not 0     | `while`   |
# | Count items in a list            | `for`     |

# ************************************ WHILE LOOP ********************************************
# while bool_expr:
#       the syntax for while loop

# if 1 < 3: # since this is true, it will print 
#     print("Hello to the world")

# A program that prints Hello to the world indefinitely
# while 1 < 3:  # this will keep printing repeatedly as long as the statement is true. It is called Infinite loop
#     print("Hello to the world")

# # A program that accepts an input from the user and prints out what the person entered and keeps doing that continously

# while True:
#     user_input = input("Enter something: ")
#     print(f"What you supplied is: {user_input}")

# A program that keeps asking for your first name and last name and then prints "Your full name is........."

# while True:
#     first_name = input('Enter firstname: ')
#     last_name = input('Enter lastname: ')
#     fullname = first_name + last_name
#     print(f" Your fullname is  {fullname}")

# A program that infinitely asks the user to enter two numbers and then prints the first number raised to the power of the second number

# while True:
#     first_num = int(input('Enter number: '))
#     second_num = int(input('Enter number: '))
#     result = first_num ** second_num
#     print(f" {first_num} raised to power of {second_num} is {result} ")

# import getpass
# while True:
#     username = input('Username: ').strip()  # ------> to remove spaces at the left and right side
#     if len(username) > 0:
#         break  # only stop looping if the condition is true
# while True:
#     password = getpass.getpass("Password: ")    # this won't make our password be visible
#     if len(password) >= 8 and len(password) <= 32:
#         break

# print(f' Your username is: {username}')
# print(f' Your password is: {password}')




# A program that keeps asking the user to enter a positive number if they provide anything negative. If the number is positive.  Say Number accepted and stop the loop

# while True:
#     num = int(input("Enter a number: ")) 
#     if num > 0:
#         print("Number accepted")
#         break
#     else:
#         print("Number must be greater than 0")

# A program that keeps asking the user to enter the price of items they bought one after the other. And when they feel like stopping, we give them a total amount of all items prices they have entered.
# total_price = 0
# while True:
#     price = float(input('Enter price of item: '))
#     total_price += price
#     print(total_price)

#     choice = input('Do you want to still enter another item?: ')

#     if choice in ['no', 'n', 'exit']:
#         break
# print("The total amount of all items prices: ", total_price)

# A program that keeps asking the user to provide programming languages and then you add them to a list. When they no longer have any idea of any other programing language, stop the loop and print out the all the the languages they have supplied.

# languages = []

# while True:
#     language = input("Enter a programming language ('done' to stop): ")

#     if language.lower() == "done":
#         break

#     languages.append(language)

# print(f"The programming languages you entered are: {languages}")

# ****************************OR****************************** 

# languages = []
 
# while True:
#     user_input = input('Enter a programming language: ')
#     languages.append(user_input)

#     choice = input('Do you wish to continue?: ')
#     if choice in ["no", 'n', 'exit']:
#         break
# print('The programming languages the user supplied are: ', languages)


# A counter
# A loop
# When the loop is executed, we increment that counter

# counter = 0
# while counter <= 10:
#     print(f"{counter} Hello World")
#     counter += 1

# A program that asks the user for their name five times and each time we get a name, we print just the first and last letters of that name.

# counter = 1
# while counter <= 5:
#     name = input('Enter your name: ')
#     print(f"{name[0]} {name[-1]}")
#     counter += 1

# A program that asks runs five times. And every single time, then ask the user for two numbers and calculate/print the average of the two numbers.

# counter = 1
# while counter <= 5:
#     num1 = int(input("Enter any number: "))
#     num2 = int(input("Enter any number: "))
#     print((num1 + num2) / 2)
#     counter += 1


# names = ["Martha", "Keylow", "David", "Kyle", "Tobi", "Dele", "Ope", "Fanning", "Kemi"]
# i = 0 
# while i < 3:
#     print(names[i]) # this will give us the name at index 0, 1, 2 that's Martha, Keylow, David
#     i += 1
# i = 0
# while i < len(names): # Run a loop going from 0 to the length of names
#     print(names[i])
#     i += 1

# artist = "ariana"
# Write a program that prints each character of this string one by one on a different lines.
# The code below will print all the characteristics at all available indexes and also give index error because we also tried to get the character at the index of the actual length of the string.
# i = 0
# while i <= len(artist):
#     print(artist[i])
#     i += 1

# Correct solution
# i = 0
# while i < len(artist):
#     print(artist[i])
#     i += 1

# animals = ["lion", "cheetah", "tiger", "leopard", "cleopatra"]
# Print the first and last letters of each animal here


# animals = ["lion", "cheetah", "tiger", "leopard", "cleopatra"]
# i = 0
# while i < len(animals):
#     print(animals[i][0], animals[i][-1])
#     i += 1

# Write a program that prints 1 to 7 and after that, print Completed
# from time import sleep
# i = 1 

# while i <= 7:
#     print(i)
#     i += 1
#     sleep(10)
# print("Completed")

# A countdown program that goes from 5 to 0 and says "Bomb activated!"

# i = 5
# while i >= 0:
#     print(i)
#     i -= 1
# print("Bomb activated")

# Write a program that prints all numbers btw 60 and 18 in descending order
# i = 60
# while i >= 18:
#     print(i)
#     i -= 10 # this means by step of 10 instead of the default ny step of 1

# A program that asks the user for a specific number and then prints all numbers from 1 up to that specified number.
# number = int(input('Enter a number: '))
# i = 1
# while i <= number:
#     print(i)
#     i += 1

# A program that prints only even numbers btw 0 and 20
# i = 0
# while i <= 20:
#     print(i)
#     i += 2

# A program that prints only even numbers btw 13 and 37
# i = 13
# while i <= 37:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("Number is ODD")
#     i += 1

# Print only even numbers from 2 to 10 (do not use +=2)
#Expected Output:
# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("Number is ODD")
#     i += 1

# OR if we weren't specifically told not to use +=2, this would have been:
# i = 2
# while i <= 10:
#     print(i)
#     i += 2

# Write a program that asks users to guess a number 5 times and if they guess correctly, we print you win or lose.
# from random import randint

# This is the normal way without using loop
# comp_num = randint(1, 10)
# user_guess = int(input('Guess a number: '))

# if comp_num == user_guess:
#     print("You win!")
# else:
#     print("You lose")

# Correct solution using loop

# i = 1
# while 1 <= 5:
#     comp_num = randint(1, 10)
#     user_guess = int(input('Guess a number: '))

#     if comp_num == user_guess:
#         print("You win!")
#     else:
#         print("You lose")

#     i += 1

# The same guess game program with tracking of user score. Give them 10 marks for every guess that is correct.
# i = 1
# total = 0
# while 1 <= 5:
#     comp_num = randint(1, 5)
#     user_guess = int(input('Guess a number: '))

#     if comp_num == user_guess:
#         print("You win!")
#         total += 10
#     else:
#         print("You lose")
    
#     i += 1

# print(f"Your total score: {total}")

# Write a program that askes the user to enter a string and then count how many vowels are in the string.
# sentence = "the quick brown fox jumps over the lazy dog"
# vowels = "aeiou"
# vowels_count = 0
# i = 0
# while i < len(sentence):
#     print(sentence[i]) # this will print every charcters not just vowels
#     i += 1

# the normal way to go about it

# i = 0
# while i < len(sentence):
#     if sentence[i] in vowels:
#         vowels_count += 1
#     i += 1
# print("Number of vowels found: ", vowels_count)


# sentence = "the quick brown fox jumps over the lazy dog"
# Write a program that uses a while loop to count how many o's we have in sentence.
# count = 0
# i = 0
# while i < len(sentence):
#     if sentence[i] == 'o':
#         count += 1
#     i += 1
# print("Number of O's found: ", count)


# Create another list that will contain ONLY words that are least five letters long. USE A WHILE LOOP
# words = ["tenet", "bright", "draw", "blue", "dark", "orn", "is", "see"]
# words_with_at_least_five_chars = []

# i = 0
# while i < len(words):
#     selected_word = words[i]
#     if len(selected_word) >= 5:
#         words_with_at_least_five_chars.append(selected_word)
#     i += 1
# print("The following is a list of words with a least 5 characters: ", words_with_at_least_five_chars)


# *************************************** FOR LOOPS ********************************************
# Very small summary

# range() follows this pattern:

# start included
# stop not included
# step tells it how to move

# for i in range(1, 11): # this means our program will run 10 times
#     n_1 = int(input('Enter a number: '))
#     n_2 = int(input('Enter a number: '))
#     addition = n_1 + n_2
     
#     print(f" {n_1} + {n_2} = {addition} ")

# Write a for loop that prints numbers from 30 - 50
# for i in range (30, 51):
#     print(i)

# A loop that runs from 0 - 6
# for i in range (0, 7):
#     print(i)

# *********OR*********

# for i in range (7): # Leaving out the starting point automatically makes it start from zero by default
#     print(i)

# A for loop that goes from 2 - 30 but picks every second number (2 and 30 inclusive)

# for i in range (2, 31, 2): # this means go by step of 2 from 2 - 31 which will give us 2 - 30 normally by step of 2
#     print(i)

# for i in range(1): # this will it run 1 time but the value of i will be 0
#     print(i)

# for i in range(6):           # 0, 1, 2, 3, 4, 5-------> number of times will run, that's 6 times 
#     name = input("Enter your name: ")
#     print(f"Your name: {name * i}") # this is replication and it will replicate it, which means i will be ) at first, then 1, 2, 3, 4, 5

# A program that asks a user and replicate it the number of times the loop has run


# A program to print right angled triangles
# for i in range(1, 11):
#     print("*" * i)


# # A loop that goes in descending order
# for i in range(60, 20):
#     print(i)   # automatically will not run because of the index 1 by default. Since it's suppose to go from lowest to the highest by 1 but if you specifically tell Python to go by step -1 then it will work and then it goes from 60 to 21(stops before the last number)

# # A loop that goes in descending order
# for i in range(60, 19, -2):     # values inside a function are called arguments
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, 0, -1):
#     print("*" * i)

# Use a for loop to print my multiplication table 4
# for i in range(1, 13):
#     print(f"4 x {i} = {4 * i}")


# This for loop prints each character of our string one by one 
# college = "SQI College of ICT"
# for i in range(len(college)):
#     print(i)

# # This for loop prints each character of our string 4 times each
# college = "SQI College of ICT"
# for i in range(len(college)):
#     print(college[i])

# Write a program that takes a string from the user , and prints each character of that user's input 6 times.
# user_input = input('Enter a string: ')
# for i in range(len(user_input)):
#     print(user_input[i] * 6) # this wil give us each character specifically

# user_input = input('Enter a string: ')
# for i in range(len(user_input)):
#     print(user_input[i] * 6, end='*') # this means it will print our print statement on the same line and of course you can have different things in our string.

# animals = ['Cheetah', 'Kangaroo', 'Lion', 'Tiger', 'Honey Badger', 'Mongoose']
# for i in range(len(animals)):
#     print(animals[i][-1])

# ****************For - each loop******************* this is what our instructor prefer calling it, python calls is loop still
# animals = ['Cheetah', 'Kangaroo', 'Lion', 'Tiger', 'Honey Badger', 'Mongoose']
# for animal in animals:
#     print(animal)   # For every animal you can find in our animals list, do what is in the loop and you can do this on either string,list, dictionary, set but you can't loop through integers, so if you need to loop throgh an integer, best bet you typecast it to a string

# numbers = [3, 4, 5, 6, 7, 8, 9] # this will work since its a list
# for num in numbers:
#     print(num)

# members = [3, 4, 5, 6, 7, 8, 9]
# members_cube = []
# for num in members:
#     members_cube.append(num ** 3)
# print(members_cube)

# footballers = ["Essien","Ronaldo", "Lampard", "Hazard", "Mikel Obi", "Rooney"]
# # Print out only footbllers that have 'a' in their names

# for footballer in footballers:
#     if "a" in footballer.lower():
#         print(footballer)

# ORRRRRRRRRR using range -----------> If you don't want to use for each loop

# for i in range(len(footballers)):
#     if 'a' in footballers[i].lower():
#         print(footballers[i])

# A program that gives us all 4 digits numbers (every combination of 4 digits that is possible)
# for i in range(10_000): # this will give us 0-999
#     print(i)

# for i in range(100): # this will give us 0-99, in range we are counting the zeros not 1. Try this out at home
#     print(f"{i}".zfill(2))  # this will give zeros from the left by the number of z-fills which means .zfill(4)-- this means all of you no matter what, have 4 values and so on.

# for i in range(10_000): # this will give us 0-999
#     print(f"{i}".zfill(4)) # this will give us all 4 digits numbers (every combination of 4 digits that is possible) but in 4 values, so it's not as if we'll have 2 values or 3 values, everything will be in 4 values



# **************Enumerate function******************enumerate()

# basketballers = ["Kobe Bryant", "Lebron James", "Steph Curry", "Michael Jordan", "Kevin Durant"]
# for basketballer in basketballers:
#     print(basketballers)

# anytime you enumerate you will get back a tuple with a number asssigned to them
# basketsballers = ["Kobe Bryant", "Lebron James", "Steph Curry", "Michael Jordan", "Kevin Durant"]
# for basketballer in enumerate(basketsballers):
#     print(basketballer)

# lets unpack the tuple straightup and to do that you make use of position
# basketballers = ["Kobe Bryant", "Lebron James", "Steph Curry", "Michael Jordan", "Kevin Durant"]
# for position, basketballer in enumerate(basketballers):
#     print(f"{position}. {basketballer}") # you can call it any other name, it's not a must you use position


# questions_bank = [
#     {'question': "What type is returned when two lists are concatenated?", 'options': ['a. List', 'b. String', 'c. Error'], 'answer': 'a'},

#     {'question': 'Who created Python programming language?', 'options': ['a. Tobi Dada', 'b. Dennis Ritchie', 'c. Guido Van Rossum'], 'answer': 'c'},

#     {'question': 'Is Python an interpreted or compiled language?', 'options': ['a. Interpreted', 'b. Compiled', 'c. No Idea'], 'answer': 'a'},

#     {'question': 'Is Python a strongly typed or loosely typed language?', 'options': ['a. Strongly typed', 'b. Loosely typed', 'c. No Idea'], 'answer': 'b'},

#     {'question': 'What symbol is used to concatenate two lists in Python?', 'options': ['a. +', 'b. &', 'c.*'], 'answer': 'a'},

#     {'question': 'Which data type is used to store multiple items in a single variable?', 'options': ['a. Integer', 'b. List', 'c. Boolean'], 'answer': 'b'},

#     {'question': 'which keyword is used to define a function in Python?', 'options': ['a. func', 'b. def', 'c. function'], 'answer': 'b'},

#     {'question': 'Which of these is a valid Python variable name?', 'options': ['a. 1name', 'b. name_1', 'c. name-1'], 'answer': 'b'},

#     {'question': 'What is the output of print (2 * 3)?', 'options': ['a. 6', 'b. 8', 'c. 9'], 'answer': 'b'},

#     {'question': 'Which keyword is used for a conditional statement in Python?', 'options': ['a. if', 'b. for', 'c. while'], 'answer': 'b'},

#     {'question': 'What is the correct file extension for Python files?', 'options': ['a. .pt', 'b. .py', 'c. .python'], 'answer': 'b'},

#     {'question': 'Which function is used to get input from the user?', 'options': ['a. get()', 'b. input()', 'c. read()'], 'answer': 'b'},

#     {'question': 'What does len() function do?', 'options': ['a. Returns length', 'b. Deletes items', 'c. Adds items'], 'answer': 'b'},

#     {'question': 'Which loop is used when the number of iterations is known?', 'options': ['a. while loop', 'b. for loop', 'c. do - while loop'], 'answer': 'b'},

#     {'question': 'Which data type is used to store True or False values in Python?', 'options': ['a. String', 'b. Boolean', 'c. .python'], 'answer': 'b'},

# ]
# total_score = 0
# for qst_num, question in enumerate(questions_bank, start = 1):   # we are using enumerate for numbering
#     print(f"{qst_num}. {question['question']}")  # the qst_num will help us with the numbering 
#     print('\n'.join(question['options']))
#     answer = input("Your answer: ")
#     if question['answer'] == answer:
#         total_score += 5
#         print(f"Correct answer. Your current score is {total_score}")
#     else:
#         print(f"Incorect answer. Your current score is {total_score}")
#         total_score -= 2

# Update the program above to have ten other coding questions with options. [Total: 15 questions]. Then for each question, make sure you track the score of the users. For every wrong anwer, deduct 2 marks. For every right answers.

# Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# for i in range(2, 11):
#     if i % 2 == 0:
#         print(i)

# ***** OR********

# for i in range(1, 11, 2):
#     print(i)

# Print a square of stars
# Ask the user to enter a number

# length = int(input("Enter a number: "))

# for i in range(length):
#     print("*" * length)
#  adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for i in matrix:
#     for j in i:
#         print(j)

# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin", "zebra"]

# smallest = min(adjectives, animals, key=len)

# print(smallest)

# for i in range(len(smallest)):
#     adj = adjectives[i]
#     animal = animals[i]

#     print(adj, animal)


# print(list(enumerate(adjectives)))
# print(list(zip(adjectives, animals)))

# print(list(range(1, 7)))

# for i in range(1, 7):
#     print(i)


# for items in zip(adjectives, animals):
#     adj, animal = items
#     print(adj, animal)

# for adj, animal in zip(adjectives, animals):
#     print(adj, animal)


# is_happy = False

# if is_happy:
#     pass    

# print("End of file")


# for i in [1, 2, 3, 4, 5]:
#     pass

# print("End of file")


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12.
# number = int(input("Enter a number: "))

# for i in range(1, 13):
#     print(f"number x {i} = {number * i}")

# text = input('Enter an input: ')

# new_word = ''

# for i in range(len(text)):
#     if i % 2 == 0:
#         new_word += text[i].upper()
#     else:
#         new_word += text[i].lower()

# print(new_word)


# Print a word like this: LiMiTleSs, hint; the uppercase occurs at the even numbers
# word = input("Enter a word: ")

# result = ""

# for i in range(len(word)):
#     if i % 2 == 0:
#         result += word[i].upper()
#     else:
#         result += word[i].lower()

# print(result)


# word = input("Enter a word: ")
# to_upper = True
# result = ""

# for i in range(len(word)):
#     if to_upper:
#         result += word[i].upper()
#     else:
#         result += word[i].lower()
#     to_upper = not(to_upper)

# print(result)



# *********************** LIST COMPREHENSIONs ***********************
# [expression for item in sequence if condition]
# words = ["random", "terrible", "chalk", "dirt", "fool", "hippoppotamus"]
# [6, 8, 5, 4, 4, 13]
# len_words = [len(word) for word in words]
# print(len_words)

# fruits = ["apple", "banana", "cherry", "date", "eggplant"]
# fruits_copy = fruits.copy()
# fruits_upper = []

# for fruit in fruits:
#     fruits_upper.append(fruit.upper())

# print(fruits)
# print(fruits_upper)
#INSTEAD OF DOING ALL THIS. YOU CAN JUST USE LIST COMPREHENSION INSTEAD
# fruits = ["apple", "banana", "cherry", "date", "eggplant"]

# fruits_upper = [fruit.upper() for fruit in fruits]

# print(fruits_upper)


# words = ["random", "terrible", "chalk", "dirt", "fool", "hippoppotamus"]

# # [6, 8, 5, 4, 4, 13]

# len_words = [len(word) for word in words]

# print(len_words)

# The generic method if you don't want to use list comprehension
# len_words = []

# for word in words:
#     len_words.append(len(word))
# print(len_words)

# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]

# [1, 2, 0, 2, 3, 1, 3, 2]


# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]

# developed_countries = ["USA", "Australia", "Japan"]

# developing_countries = [country.upper() for country in countries if country not in developed_countries]

# print(developing_countries)

# ********************************** LIST COMPREHENSIONs ************************************

# QUICK WORK ON LIST COMPREHENSION
# Count the number of 'a' in each country in countries using list comprehension
# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]
# new_word = [country.lower().count('a') for country in countries]
# print(new_word)
# [1, 2, 0, 2, 3, 1, 3, 2] # --------------> Expected outcome, when you count the number of 'a's

#OR

# new_list = []
# for country in countries:
#     new_list.append(country.lower().count('a'))
# print(new_list)
# [1, 2, 0, 2, 3, 1, 3, 2] # --------------> Expected outcome, when you count the number of 'a's


# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]
# developed_countries = ["USA", "Australia", "Japan"]
# developing_countries = [country.lower() for country in countries if country not in developed_countries]
# print(developing_countries)


# numbers = [1, 8, 34, 76, 55, 43, 29, 38]
# odd_numbers = [number for number in numbers if number % 2 != 0]
# print(odd_numbers)

# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# not_hausa = [tribe for tribe in tribes if tribe != 'Hausa']
# print(not_hausa)

# OR

# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# not_hausa = []

# for tribe in tribes:
#     if tribe != "Hausa":
#         not_hausa.append(tribe)

# startwith_letter_I = [tribe for tribe in tribes if tribe.lower().startswith('i')]
# print(startwith_letter_I)

# Create a list of mutiples of 4 between 2 and 45 using a list comprehension
# multiples_of_4 = [num for num in range(2, 46) if num % 4 == 0]
# print(multiples_of_4)

#************* DICTIONARY COMPREHENSIONS*********************************
# when filtering (if statement), you add to the right but when transforming you add it to the beginning
# languages = ["Python", "Javascript", "Elixir", "Ruby", "C++", "Go"]

# len_languages = {language: len(language) for language in languages}
# print(len_languages)

# upper_case_languages = {language: language.upper() for language in languages}
# print(upper_case_languages)

#************* DICTIONARY COMPREHENSIONS*********************************

# -------------------------------looping through a dict-------------------------------

# states_and_capitals = {"Ondo": "Akure", "Anambra": "Awka", "Oyo": "Ibadan", "Osun": "Osogbo"}

# for state in states_and_capitals:  # this will print us the keys
#     print(state)

# for capital in states_and_capitals.values():  # this wil print us the values
#     print(capital)


# for state in states_and_capitals.keys(): # this will still print us the keys
#     print(state)

# print(states_and_capitals.keys())  # dict_keys -> list
# print(states_and_capitals.values())  # dict_values -> list
# print(states_and_capitals.items())  # dict_items -> list of tuples

# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")

# -------------------------------looping through a dict-------------------------------

# **********************************GENERATORS*********************************************
# Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# all_contains_only_uppercase = all(greeting.isupper() for greeting in greetings)
# print(all_contains_only_uppercase)

# Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
# words = ["apple", "zebra", "mango", "lemon"]
# any_word_starts_with_z = any(word.lower().startswith('z') for word in words)
# print(any_word_starts_with_z)

# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# tribe_starts_with_i = [True, False, False, False, True, True, True]
# tribe_starts_with_i = [tribe.lower().startswith("i") for tribe in tribes]
# all_start_with_i = all(tribe_starts_with_i)
# print(all_start_with_i)


# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# # # tribe_starts_with_i = [True, False, False, False, True, True, True]
# tribe_starts_with_i = (tribe.lower().startswith("i") for tribe in tribes)
# all_start_with_i = all(tribe_starts_with_i)
# print(all_start_with_i)


# print(all([True, False, False, False, True, True, True]))
# print(all([True, True, True, True]))
# print(any([True, False, False, False, True, True, True]))
# print(any([False, False, False]))
# print(all([False, False, False]))

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]

# greater_than_10 = (value > 10 for value in values)

# all_greater_than_10 = all(greater_than_10)

# print(all_greater_than_10)

# OR ---------> You can do it straightup instead
# values = [5, 12, 3, 18, 7]

# all_greater_than_10 = all(value > 10 for value in values)

# print(all_greater_than_10)


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
# names = ["John", "Sara", "Mike", "Amnd"]

# any_name_contains_a = any("a" in name.lower() for name in names)

# print(any_name_contains_a)
# Rule to remember:

# all(condition for item in items) checks if every item satisfies the condition
# all(item for item in items if condition) first filters items, then checks whether the remaining items are truthy

#*************************ASSIGNMENT*******************************
# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# password = ["Password123!"]
# strong_password = []

# DO NOT USE REGEX.
#*************************ASSIGNMENT*******************************

# ***************************************GENERATORS*************************************************

