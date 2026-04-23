# ******************* Conditional Statements****************
# (If statement) --->

# print("Hello to the world")
# number = int(input("Enter your number: "))

# user = input("Enter your username: ")
# if number > 15:   # As long as it's (true) it will always run but if it's false it won't run
    
    # print(user * 10)
# else:   # this means if the (if) is false it will automatically come to the (else) statement but if the (if) runs the (else) will not run
    # input("enter your password: ")

# print ("Program finished") # this will run because it's not under the (if statement), so it will skip the conditional statement then run the next program


# Quick work
# A program that asks the user to enter their age and then tell if they are eligible to vote

# age = int(input("Enter your age: "))

# if age>= 18:   # if age>= 18: and age <= 80:  ------> this means you have to be between 18 and 80
    # print("You are eligible to vote")
# else:
#     print("Sorry you are not eligible to vote.")

# QUESTION: Write a program that takes two numbers from the user. Then tell us if the addition of the two numbers is greater than 20 or not.

# first_response = int(input('Enter any number: '))
# second_response = int(input('Enter any number: '))

# if first_response + second_response > 20:
#     print(f" The addition of {first_response} and {second_response} is greater than 20")
# else:
#     print(f"The addition of {first_response} and {second_response} is lesser than 20")

# QUESTION: Write a program that tells whether a specific chracter in the vowels or not
# vowels = "aeiou"

# if 'b' in vowels:
#     print('b is IN a vowel')
# else:
#     print('b is NOT a vowel')

# # OR

# vowels = "aeiou"
# char = input('Enter any vowel: ').lower()
# if char in vowels:
#     print("Char is a Vowel")
# else:
#     print("Char is not a vowel")

# QUESTION: Write a program that takes a number from the user and then tell if that number is between 20 and 300
# number = int(input("Enter your number: "))
# user_input = int(input('Enter any number: '))
# if user_input >= 20 and user_input <= 300:
#     print(f" The {user_input} is between 20 and 300")
# else:
#     print(f" The {user_input} is not between 20 and 300")



# QUESTION: Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".

# colors_inputted_by_user = set(input('Enter three colors seperated by comma: ').split(', '))
# primary_colors = {"red", "blue", "yellow"}
# if colors_inputted_by_user == primary_colors:
#     print(f" The colors inputted by the user are all primary colors.")
# else:
#     print(f" The colors inputted by the user are not primary colors.")

# #Or
# primary_colors = {"red", "blue", "yellow"}
# color1 = input("Enter primary color: ")
# color2 = input("Enter primary color: ")
# color3 = input("Enter primary color: ")

# user_colors_set = {color1, color2, color3}
# if user_colors_set == primary_colors:
#     print("They are all primary colors")
# else: 
#     print("Not all primary colors")


# filename = input('Enter a file name: ')
# if filename.endswith(".jgp") or filename.endswith(".png") or filename.endswith(".gif"):
#     print("Image file")
# else:
#     print("Not an Image file")


# #OR

# filename = input("Enter your file name: ")
# if filename.endswith(('.jgp', '.png', '.gif')):
#     print("Image file")
# else:
#     print("Not an image file")


# Write a program that takes a number and if the number is btw 10 and 15, we display"Low Number", if it is btw 16 and 25, we say "Still Low", if btw 26 and 50, we say "Moderate", and if it is higher than  50, we say "Very good"

# num = int(input('Enter any number: '))
# if num >= 10 and num <= 15:
#     print("Low Number")
# elif num >= 16 and num <=25:
#     print("Still Low")
# elif num >= 26 and num <= 50:
#     print("Moderate")
# elif num > 50:
#     print("Very good")
# else: 
#     print("Not available")


# You have two variables, status1 and status2, provided through user input, each of which can be "active", "inactive", or "pending". Write an if statement to print "both active". If both statuses are "active", "one active", if exactly one is "active", add "none active" if neither is active
# status1 = input('Enter a status: ')
# status2 = input('Enter a status: ')
# if status1 == "active" and status2 == "active":
#     print('both active')
# elif status1 == "active" and status2 != "active":
#     print('one active')
# elif status1 != "active" and status2 == "active":
#     print('One active')
# elif status1 != "active" and status1 != "active":
#     print('None active')
# else:
#     print("Pending")


# # #OR

# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print('one is active')
# else:
#     print('None active')



# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# mode = input('Enter a mode: ').lower()
# if mode == "manual":
#     print('Manual mode activated')
# elif mode == "automatic":
#     print('Automatic mode activated')
# elif mode == "off":
#     print("System is off")
# else:
#     print("Oops, try again later")




# pass in python  -------> The pass keyword in pythin is used when you have a block of code where you don't know what to write and you dont want python to throw an error
# a = 265
# b = 23

# if b > a:
#     print("No, B is lesser than A")   # make use of "pass" here since you dont know what to write
# elif a == b:
#     print("A is equal to B")
#     print("A is equal to B")
#     print("A is equal to B")
#     print("A is equal to B")
#     print("A is equal to B")
#     print("A is equal to B")
# else:
#     pass


# Nested If ------> It's basically an "if" statement that is in another "if" statement (just like nested list and  nested dictionary)

# Write a program that takes a gender and age from the user, and if they are male and between the age 15-17, we should say "Almost eligible to vote". If they are males and between 18-20, say "Eligible to vote, but we suggest you become 21 years first". If the male is between 21-60, say "Go and vote now". And if the male is over 60, say "You sef don try......Go retire."
#If they are females and between ages 18-22, "You cannot vote just yet". If between 23-40, say "Elgible to vote". If Older than 40, say too old to vote now.

# gender = input('Enter your gender: ')
# age = int(input('Enter your age: '))

# if gender == 'male' and age >= 15 and age <= 17:
#     print('Almost eligible to vote')
# elif gender == 'male' and age >= 18 and age <= 20:
#     print('Eligible to vote but we suggest you become 21 years first')
# elif gender == 'male' and age >= 21 and age <= 60:
#     print('Go and vote now')
# elif gender == 'male' and age > 60:
#     print('You sef don try.....Go retire')
# elif gender == 'female' and age >= 18 and age <= 22:
#     print('You cannot vote just yet')
# elif gender == 'female' and age >= 23 and age <= 40:
#     print('Eligible to vote')
# elif gender == 'female' and age > 40:
#     print('Too old to vote now')
# else:
#     print('Not even eligible to vote')


# OR Use NESTED If here:
# Write a program that takes a gender and age from the user, and if they are male and between the age 15-17, we should say "Almost eligible to vote". If they are males and between 18-20, say "Eligible to vote, but we suggest you become 21 years first". If the male is between 21-60, say "Go and vote now". And if the male is over 60, say "You sef don try......Go retire."
#If they are females and between ages 18-22, "You cannot vote just yet". If between 23-40, say "Elgible to vote". If Older than 40, say too old to vote now.

# gender = input('Enter your gender: ')
# age = int(input('Enter your age: '))

# if gender == "male":
#     if age >= 15 and age <= 17:
#         print('Almost eligible to vote')
#     elif age >= 18 and age <= 20:
#         print('Eligible to vote but we suggest you become 21 years first')
#     elif age >= 21 and age <= 60:
#         print('Go and vote now')
#     elif age > 60:
#         print('You sef don try.....Go retire')
#     else:
#         print('Commot for here')

# elif gender == "female":
#     if age >= 18 and age <= 22:
#         print('You cannot vote just yet')
#     elif age >= 23 and age <= 40:
#         print('Eligible to vote')
#     elif age > 40:
#         print('Too old to vote now')
# else: 
#     print("Not even eligible to vote")



# # A simple guess game
# # The computer already has a randomly generated number in mind
# import random
# computer_number = random.randint(1, 10)
# user_guess = int(input('Guess the number: '))
# print("Hint: ", computer_number * 3)
# if computer_number == user_guess:
#     print('Correct guess!!!')
# else: 
    # pass # you can use the "pass" here if you're not trying to write an exact figure or word and you don't want pyhton to see as indentation error. or;
    # print(f"Hmmmm. Incorrect. The correct number is {computer_number}")

# Rewrite the same program but try to allow the user to know if their guess is bigger than the computer's number. And if it is lower than the computer number, let them know. Otherwise, tell them their guess is right.

# import random

# computer_number = random.randint(1, 10)
# print("Hint: ", computer_number * 3)
# user_guess = int(input('Guess the number: '))
# if user_guess > computer_number:
#     print("It is bigger than computer's guess")
# elif user_guess < computer_number:
#     print("It is lesser than computer's guess")
# else:
#     print("Correct guess") 

# import random

# questions_bank = [
#     {'question': "What type is returned when two lists are concatenated?", 'options': ['a. List', 'b. String', 'c. Error'], 'answer': a},
#     {'question': "Who created Pyhton programming langauge?", 'options': ['a. Tobi Dada', 'b. Dennis Rtchie', 'c. Compiled', 'c. No Idea'], 'answer': a}
# ]

# chosen_question = random.choice(questions_bank)

# print(chosen_question['question'])
# print('\n'.join(chosen_question['options']))

# user_answer = input().lower()

# if user_answer == chosen_question['answer']:
#     print("Correct!! One sweet for you")
# else:
#     print("Nothing for you")


# We build a jumbled guess game
# import random
# words = ["helicopter", "biscuit", "encyclopedia", "dictionary", "aeroplane"]
# chosen_word = random.choice(words)
# words_to_list = list(chosen_word)
# random.shuffle(words_to_list)
# print(f"Here is the word of the day for you: {words_to_list}")

# answer = input('Enter the correct word: ')
# if answer == chosen_word:
#     print(f"Wow! Congratulations!!! The correct answer is: {chosen_word}")
# else:
#     print(f"Hmm. Sorry, you got it wrong. The correct answer is: {chosen_word}")

# QUICK QUESTION 
# import random

# comp_1 = random.randint(1, 6)
# comp_2 = random.randint(1, 6)
# total_comp = comp_1 + comp_2

# user_1_guess = random.randint(1, 6)
# user_2_guess = random.randint(1, 6)
# total_user_guess = user_1_guess + user_2_guess
# print(f"The total of computer guess is {total_comp} and the total of user guesses is {total_user_guess}")

# if total_user_guess > total_comp:
#     print(f"Congratulations!! You won!!!")
# elif total_user_guess < total_comp:
#     print(f"Oops! You lost. Try again later!!!")
# else:
#     print("It's a draw!!!")


# QUICK QUESTION: Write a program to calculate BMI. Ask the user for weight  (kg), height (m), and age. Use the formula BMI = weight / (height * height ). If BMI is less than 18.5, display Underweight. If BMI is between 18.5 and 24.9, display Normal weight, but if the user is older than 50, display Normal weight (monitor health regularly) instead. If BMI is between 25 and 29.9, display Overweight. If BMI is 30 or above, display Obese, but if BMI is greater than 35, display Severely Obese. Use only if and nested if statements. height and weight cannot be zero.

# user_weight = float(input('Enter weight: '))
# user_height = float(input('Enter height: '))
# user_age = int(input('Enter age: '))

# BMI = user_weight / (user_height * user_height)

# if BMI < 18.5:
#     print("Underweight")

# elif BMI >= 18.5 and BMI <= 24.9:
#     if user_age > 50:
#         print("Normal weight(monitor health regularly)")
#     else: 
#         print("Normal weight")

# elif BMI >= 25 and BMI <= 29.9:
#     print("Overweight")
# elif BMI >= 30:
#     print("Obese")
# elif BMI > 35:
#     print("Severely Obese")


# QUICK QUESTION: A program that takes two numbers and divides the first by the second number. WITHOUT ANY ERRORS.

# How to solve this:

# Check first that the user's input only contains numbers before typecasting
# After converting successfully, check that the second number is not 0.

# num1 = (input('Enter any number: '))
# num2 = (input('Enter any number: '))

# if num1.isdigit() and num2.isdigit():
#     num1 = float(num1)
#     num2 = float(num2)

#     if num2 == 0:
#         print("Second number should not be zero")
#         exit()

#     else:
#         print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("Your inputs should only be numbers")

# division = num1 / num2
# print(f"The division of {num1} by {num2} is {division}")


# QUICK QUESTION: Ask the user to enter the number of passengers and the current year. The program should first check if the car is registered; if it is not, display "Car cannot be driven on the road" and stop. If the car is registered, the program should then check if the car insurance; if it does not, display "Car cannot be driven without insurance" and stop. If the car is allowed on the road, the program should check the car year: if the car is more than 20 years old, display "Car must go for inspection first". Otherwise, the program should check the fuel type: electric cars can carry a maximum of 4 passengers, while petrol cars can carry a maximum of 6 passengers. If the passenger count exceeds the allowed number, display "Too many passengers", otherwise display "Trip approved".

# cars = [
#      {"brand" : "Toyota", "fuel_type" : "petrol", "year" : 2018, "is_registered" : True, "has_insurance" : True},
#     {"brand" : "Tesla", "fuel_type" : "electric", "year" : 2022, "is_registered" : True, "has_insurance" : False},
#     {"brand" : "Honda", "fuel_type" : "petrol", "year" : 2000, "is_registered" : True, "has_insurance" : True},
#     {"brand" : "Hyundai", "fuel_type" : "petrol", "year" : 2015, "is_registered" : False, "has_insurance" : True},
#     {"brand" : "BMW", "fuel_type" : "electric", "year" : 2019, "is_registered" : True, "has_insurance" : True},
#     {"brand" : "Nissan", "fuel_type" : "petrol", "year" : 2003, "is_registered" : True, "has_insurance" : False}
# ]

# print(f"We have {len(cars)} cars in our collection. Please choose one: ")
# user_option = int(input())
# selected_car = cars[user_option]

# num_of_passengers = int(input('Enter number of passengers: '))
# current_year = int(input('Enter current year: '))

# if not selected_car['is_registered']:
#     print("Car cannot be driven on the road")
#     exit()

# else:
#     if not selected_car['has_insurance']:
#         print("Car cannot be driven without insurance")
#         exit()

#     age_of_car = current_year - selected_car['year']
#     if age_of_car > 20:
#         print("Car must go for inspection first")
#     else:
#         if selected_car['fuel_type'] == 'electric':
#             if num_of_passengers > 4:
#                 print("Too many passengers")
#             else:
#                 print("Trip approved")
#         elif selected_car["fuel_type"] == 'petrol':
#             if num_of_passengers > 6:
#                 print("Too many passengers")
#             else:
#                 print("Trip approved")
            


# Write a program that takes a string from a user and if the string has even number number of letters, print the first half of the string. Otherwise, print the full string

# user_string = input("Enter a string: ")

# if len(user_string) % 2 == 0:
#     print(user_string[:len(user_string) // 2])
# else:
#     print(user_string)

# #OR

# user_string = input("Enter a string: ")
# first_half = len(user_string) // 2

# print(user_string[:first_half])

# if len(user_string) % 2 == 0:
#     print(user_string[:first_half])
# else:
#     print(user_string)



# Random Password generator
# import random
# import string

# has_letters = input("Do you want letters included? (y/n): ")
# has_digits = input("Do you want digits included? (y/n): ")
# has_symbols = input("Do you want symbols included? (y/n): ")

# password = []
# if has_letters in ['yes', 'y']:
#     random_letters = random.sample(string.ascii_letters, 8)
#     password.extend(random_letters)
# if has_digits in ['yes', 'y']:
#     random_digits = random.sample(string.digits, 4)
#     password.extend(random_digits)
# if has_symbols in ['yes', 'y']:
#     random_symbols = random.sample(string.punctuation, 4)
#     password.extend(random_symbols)
# if len(password) < 1:
#     print("No password generated")
#     exit()
# random.shuffle(password)

# full_password_string = ''.join(password)
# print(f"Your generated password is: {full_password_string}")

# Write a program that allows the user to choose whether they want a username to contain lowercase letters, uppercase letters, digits, or all.
# import random
# import string
# has_lowercase_letters = input('Do you want lowercase included? (y, n): ').lower()
# has_uppercase_letters = input('Do you want uppercase included? (y, n): ').lower()
# has_digits = input('Do you want digits included? (y, n): ').lower()

# username = []
# if has_lowercase_letters in ['yes', 'y']:
#     random_lowercase_letters = random.choices(string.ascii_lowercase, k = 8)
#     username.extend(random_lowercase_letters)
# if has_uppercase_letters in ['yes', 'y']:
#     random_upper_letters = random.choices(string.ascii_uppercase, k = 9)
#     username.extend(random_upper_letters)
# if has_digits in ['yes', 'y']:
#     random_digits = random.choices(string.digits, k = 5)
#     username.extend(random_digits)
# if len(username) < 1:
#     print("No username generated")
#     exit()
# random.shuffle(username)
# full_username = "".join(username)
# print(f" The preferred username is : {full_username}")

# Write a program that allows the user to choose whether they want a PIN to contain:
# digits only
# letters only
# both digits and letters
# Then ask for the length of the PIN and generate it based on their choice.

# Extra rule:
# If the user enters an invalid choice, print "Invalid choice".
# import random
# import string
# preferred_length = int(input('Enter preferred length: '))
# has_digits_only = input('Do you want it to contain digits only? (y/n): ')
# has_letters_only = input('Do you want it to contain letters only (y/n? : ').lower()
# have_both_digits_and_letters = input('Do you want it to contain both letters and digits (y/n): ').lower()
# characters = string.ascii_letters + string.digits
# PIN = []
# if has_digits_only in ['yes', 'y']:
#     random_digits = random.choices(string.digits, k = preferred_length)
#     PIN.extend(random_digits)
# elif has_letters_only in ['yes', 'y']:
#     random_letters = random.choices(string.ascii_letters, k = preferred_length)
#     PIN.extend(random_letters)
# elif have_both_digits_and_letters in ['yes', 'y']:
#     random_letters_digits = random.choices(characters, k=preferred_length)
#     PIN.extend(random_letters_digits)
# else:
#     print("Invalid Choice")
#     exit()
# random.shuffle(PIN)
# full_pin = ''.join(PIN)
# print(f"The full pin is {full_pin}")
# Then ask for the length of the PIN and generate it based on their choice.

# A simple program that registers a user with JAMB and gives them a profile code if they filed all their information.
# firstname, lastname, email, dob, origin

# from random import randint
# print("*************** WELCOME TO JAMB PORTAL*********************")
# firstname = input("First name: ").strip()  # why did we strip because I tried it without stripping and it still worked
# lastname = input("Last name: ").strip()
# email = input("Email: ").strip()
# dob = input("Date of Birth: ").strip()
# state_of_origin = input("State: ").strip()

# if not firstname or not lastname or not email or not dob or not state_of_origin:
#     print("All fields are required. Please fill them.")
#     exit()
# profile_code = randint(100_000_000, 999_999_999) # this will give us 9 digits randint(100, 999) it will randomly give us 3 digits. (10, 99)- this will give us two digits
# profile_code = randint(100_000_000, 999_999_999)
# full_name = f"{firstname} {lastname}"
# print(f"Hi, {full_name}, your generated Profile Code is: {profile_code}")


# A program that asks a user for their date of birth. E.g 27/09/1992 and then print out your output as: "You were born on September 27, 1992."
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# user_input = input(('Enter date of birth(d/m/yy): ')).split('/')
# day, month, year = user_input
# print(day, month, year)
# month = int(month)
# birth_month = (months[month -1])
# print(f" You were born on {birth_month} {day}, {year}")


#  *************** USING SHORTHAND IF *******************
# When to use the "if" statement on a single line
# first_name = input("Enter firstname: ")
# last_name = input("Enter lastname: ")

# has_fullname = "Yes" if len(first_name) > 0 and len(last_name) > 0 else "No" # this is used to assign values to variables but it's not ideal to do something like this
# print(has_fullname)

# cities = ["ibadan", "onitsha", "ondo", "benin"]
# degrees = ['bsc', 'phd']
# email_domains = ['gmail.com', 'sqi.edu.ng']

# name = input('Enter your name: ')
# degree = input('Enter your academic degree: ')
# city = input('Enter your city: ')
# email = input('Enter your email: ')
# email_domain = email.split('@')[-1]

# city_acceptance_status = "Yes" if city in cities else "No Allowed"
# degree_acceptance_status = "Yes" if degree in degrees else "Degree Not Accepted"
# email_acceptance_status = "Yes" if email_domain in email_domains else "Email Not Accepted"

# print(f"City Status: {city_acceptance_status}")
# print(f"Degree Status: {degree_acceptance_status}")
# print(f"Email Status: {email_acceptance_status}")


# Read on Matchcase

# Write a program that takes a string from the user and checks the length of the string. If the length is greater than 5, print only the last 3 characters. Otherwise, print the whole string.
# user_string = input('Enter a string: ')
# last_3_chars = (user_string)[-3:]
# if len(user_string) > 5:
#     print(last_3_chars)
# else:
#     print(user_string)


# The difference between random.sample and random.choices is:

# random.sample(population, k)
# picks unique items only, so no repeats
# random.choices(population, k=...)
# picks items with replacement, so repeats are allowed
# One small note:
# sample() also has a parameter called k, but Python allows it positionally there, while choices() expects you to write it as a keyword in this case

