import getpass
#QUESTION 1: MADLIBS( IF I WERE A PRESIDENT)

# person_in_room = input('Enter the person in the room: ')
# number = input('Enter a number: ')
# adjective = input('Enter an adjective: ')
# color = input('Enter a color: ')
# noun = input('Enter a noun: ')
# type_of_food = input('Enter a type of food: ')
# noun2 = input('Enter a noun: ')
# verb = input('Enter a verb: ')
# article_of_clothing = input('Enter an article: ')
# adjective2 = input('Enter an adjective: ')
# celebrity = input('Enter a celebrity: ')
# number2 = input('Enter a number: ')
# person_in_room2 = input('Enter a person in the room: ')
# noun3 = input('Enter a noun: ')
# person_in_room3 = input('Enter a person in the room: ')
# occupation = input('Enter your occupation: ')


# print(f"""
# #***********************IF I WERE PRESIDENT***************************************
# My name is {person_in_room} and I am {number} years old. If i were president, I'd do a whole bunch of {adjective} things:
# 1. I would drive the biggest {color} car in the country. And that car would go faster than any other {noun} car in the world!
# 2. Everyone would eat pepperoni {type_of_food} for dinner.
# 3. I would live in the Statue of {noun2} and build a {verb} pool at her feet.
# 4. I would wear a/an {article_of_clothing} on my head, and everyone would say i look {adjective2} like {celebrity}.
# 5. School would be open only {number2} days a year.
# 6. I would give my friends the best jobs. I would nominate {person_in_room2} to be secretary of (the) {noun3}, and {person_in_room3} could be vice {occupation}!
# """)



#QUESTION 2: MADLIBS ( ASKING SOMEONE OUT)

# term_of_endearment = input('Enter a term of endearment: ')
# first_name = input('Enter your first name: ')
# first_name_last_name = input('Enter your first and last name: ') 
# place = input('Enter your place: ')
# day_of_the_week = input('Enter the day of the week: ')
# adjective = input('Enter an adjective: ')
# color = input('Enter the color: ')
# item_of_clothing = input('Enter the cloth item: ')
# number = input('Enter a number: ')
# verb = input('Enter a verb: ')
# verb2 = input('Enter a verb: ')
# verb3 = input('Enter a verb: ')
# verb4 = input('Enter a verb: ')

# print(f"""
# Hey, {term_of_endearment}. It's me. What's up? You know, {first_name}, {first_name_last_name}. From the {place}. Two {day_of_the_week}s ago. I was the {adjective} guy in the {color} parachute {item_of_clothing}. I paid the bus boy {number} dollars to {verb} me your information. I was wondering if may be you'd like to {verb2} out with me. Please don't call the {verb3} department. Alright, I'll {verb4}. So, that's a no, right?
# """)

# QUESTION 3: Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# ANSWER:
# user_name = input('What is your name: ')
# print(f"Hello {user_name}!")

# Question 4: Ask the user for their birth year and calculate their age. Print the user's age in the 
#format “You are {age} years old.”.
# ANSWER: 
# b_year = int(input('What is your age: '))
# current_year = 2026
# current_age = current_year - b_year
# print(f"You are {current_age} years old.")

# Question 5: Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
#ANSWER: 
# favorite_color = input('What is your favorite color: ')
# print(f"Your favorite color is {favorite_color}.")

# Question 6: Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
#ANSWER: 
# user_word = input('Enter a word: ')
# formatted_word = user_word.lower().replace(' ', '')
# reversed_user_word = formatted_word[::-1]
# palindomic_reversed_word = formatted_word == reversed_user_word
# print(f"It is {palindomic_reversed_word} that {user_word} is a palindrome. ")

# Question 7: Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
# ANSWER: 
# password = getpass.getpass('Enter  password: ')
# length_of_password = len(password)
# is_valid = 8 <= length_of_password <= 30
#  or
# is_valid = length_of_password >= 8 and length_of_password <= 30

# print(f"It is {is_valid} that the password fufils the criteria.")

# Question 8: Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# ANSWER:
# weight = float(input('Enter your weight in kilograms: '))
# height = float(input('Enter your height in meters: '))
# body_mass_index = weight / (height ** 2)
# print(f"Your BMI is {body_mass_index:.2f}")





# Write a program that takes a person's name and then also ask them for a number. After that, replicate the person's name the number of times they've specified

# person_name = input('Enter your name: ')
# person_number = int(input('Enter your number: '))
# result = person_name * person_number
# print(result)



# Write a program that takes a word from the user, then print out the first letter of that word, concatenated with the last letter, and finally concatenated with the full string again.

# user_word = input('Enter a word: ')
# first_letter_word = user_word[0]
# last_letter_word = user_word[-1]
# concatenate_word = first_letter_word + last_letter_word
# result = concatenate_word + user_word
# print(result)

