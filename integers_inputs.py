import getpass
# age = 23
# freq = 106.5
# print(type(age))

# print(age / age)
# print(freq + age)

# #He was 23 when he started working at Faaji 106.5fm

# #Typecasting functions: int(), float(), bool(), list(), tuple(), dict(). they take a value and then turn it to another data type so you can use it
# print("He was " + str(age) + " when he started working at Faaji " + str(freq) + "fm")

# price = 2_000_000_000
# print(price)

# #Booleans
# #True
# #False
# is_raining = True
# is_not_raining = False

# print(32 + 2 > 23)
# print(5 >= 2)

# age = 30
# print(32 * 2 < 100 and age < 200 and is_raining)

# print(age == 30)
# print(age != 30)

# # A simple program that determines whether a string has exactly five characters
# word = "E lo fokan bale"
# word_length = len(word)
# has_five_letters = word_length == 5
# print(f"It is {has_five_letters} that {word} has exactly five characters")

# print(bool(0))
# print(bool(0.000))
# print(bool(' '))

# print(bool(None))
# print(bool("     ".strip()))

# book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"

# author, book_title, year_written, isbn, pages, price = book_info.split(' ; ')
# price = float(price)
# print(f"""The book {book_title.title()} was written by {author.title()} and published in {year_written}.It has {pages} pages and {isbn.replace('ISN', 'ISBN')} and costs #{price:.2f}""")




# **************** THE INPUT FUNCTION******************
# city = input('Enter city: ')
# print(f"Hello, bro, what you input is: {city}")

# ***********************PERSONAL INFORMATION************************
# name, email, age, dob, phone
# name = input("Enter your name: ")
# email = input("Enter your email: ")
# dob = input("Enter date of birth in format (yyyy-mm-dd): ")
# phone = input('Enter phone number: ')

# b_year, b_month, b_day = dob.split('-')
# b_year = int(b_year)
# current_age = 2026 - b_year

# print(f"""******************************************PERSONAL INFORMATION****************************************************************************************************
# NAME: {name}
# EMAIL: {email}
# CURRENT AGE: {current_age} years
# PHONE NUMBER: {phone}
# """)


# A program that calculates addition input from two numbers
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# result = num1 + num2
# print(result)
# print(f"{num1} + {num2}  = {result}")

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter your second number: '))
# num3 = int(input('Enter your third number: '))
# result = num1 * num2 * num3
# print(result)
# print(f"{num1} * {num2} * {num3} = {result}")

# b_year = int(input('Enter your year: '))
# current_year = 2026
# current_age = current_year - b_year
# print(current_age)

# Kilogram to pounds converter
# kg = float(input('Enter your weight (kg): '))
# pound = 2.2
# kg_to_pounds = kg * pound

# print(f"You are {kg}kg == ({kg_to_pounds:.2f}lbs)")


# ***************USING GETPASS MODULE(A PYTHON THAT HAS BEEN WRITTEN ALREADY TO MAKE THINGS EASIER FOR YOU) TO HIDE INPUTS
# print("***************FACEBOOK LOGIN PAGE ***********************")
# username = input('Enter Username: ')
# password = getpass.getpass('Enter password: ')
# cvv = getpass.getpass("Enter your CVV: ")


#Which means we don't have to write getpass twice
# from getpass import getpass
# print("***************FACEBOOK LOGIN PAGE ***********************")
# username = input('Enter Username: ')
# password = getpass('Enter password: ')
# cvv = getpass("Enter your CVV: ")


# ********************MAD LIBS GAME***********************
# plural_noun = input('Enter a plural noun (eg: rats): ')
# plural_noun2 =  input('Enter a plural noun (eg: rats): ')  
# person_last_name = input('Enter your last name: ')
# adjective = input('Enter an adjective: ')
# noun1 = input('Enter your noun: ')
# noun2 = input('Enter your noun: ')
# noun3 = input('Enter your noun: ')
# noun4 = input('Enter your noun: ')
# noun5 = input('Enter your noun: ')
# noun6 = input('Enter your noun: ')
# noun7 = input('Enter your noun: ')
# body_part1 = input('Enter a body part: ')
# body_part2 = input('Enter a body part: ')
# exclamation =  input('Enter an exclamation: ')
# verb =  input('Enter a verb: ')
# adjectives2 = input('Enter an adjective: ')
      
# print(f"""
# *********************************A VISIT TO THE DENTIST*************************
      
# A one-act play to b performed by two {plural_noun} in this room.
# PATIENT: Thank you so very much for seeing me, Doctor {person_last_name}, on such {adjective} notice.
# DENTIST: What is your problem, young {noun1}?
# PATIENT: I have a pain in my upper {noun2}, which is giving me a severe {body_part1} ache. 
# DENTIST: Let me take a look. Open your {body_part2} wide. Good. Now, I'm going to tap your {plural_noun2} with my {noun3}.
# PATIENT: Shouldn't you give me a/an {noun4} killer?
# DENTIST : It's not necessary yet. {exclamation}!! I think I see a/an {noun2} in your {noun3}.
# PATIENT: No. I'm going to {verb} your tooth and put it in a temporary {noun6}
# PATIENT: When do I come back for the {adjectives2} filling?
# DENTIST: A day after i cash out {noun7}
# """)



# ***************************OPERATORS & OPERANDS************************

# Arithmetic operators: Used to perform arithmetic operations (+, -, / (result will be in float), //(result will be in floor which means int), *, **(exponention: it means raise to power), %(modulos operator, it means tell me the reminder))
# Note; you can only use two operators with strings. +(they have to be of same type) and *(string and int)


# Assignment operators: it means to assign a value to a variable(=, +=, -=, *=, //=, /=, %=, **=)
# name = "Tobi"
# name = "Johnson"
# city = "Johannesburg"
# print(name)
# print(city)

# num1 = 30
# num1 += 80  #Let me take the former value of num1 and add 80 to it
# num1 -= 50 #Let me take the 110 and remove 50
# num1 = num1 + 80 #That will be the final value(60) plus 80
# print(num1)
# this applies to everything on operators

# Comparison operators: (>, <, <=, >==, !=, ==)
# ***************A palindromic word program eg: madam, refer, radar, mom, dad.*********************
# Steps: Accept the word from the user
# Turn the user's string to lowercase
# Reverse that user's lowered string
# user_word = input('Enter a word: ')
# formatted_word = user_word.lower().replace(' ', '')
# rv_user_word = formatted_word[::-1]
# palindomic_rv_word_user = formatted_word == rv_user_word
# print(f"It is {palindomic_rv_word_user} that '{user_word}' is a palindrome")
# print(palindomic_rv_word_user)


# Logical operators: and, or, not(It is used to combine boolean operators). we use them with boolean expressions
# at least 18 and from lagos

#Using the OR operator to give admission status based on EITHER a valid city or age
# age = int(input("Enter your age: "))
# city = input('Enter your city: ').lower()
# has_valid_age = age >= 18
# has_valid_city = city =='lagos'
# print(f"ADMISSSION STATUS: {has_valid_age or has_valid_city}")


#Using the and operator to give admission 
# age = int(input("Enter your age: "))
# city = input('Enter your city: ').lower()
# has_valid_age = age >= 18
# has_valid_city = city =='lagos'
# print(f"ADMISSSION STATUS: {has_valid_age and has_valid_city}")

# A program that takes a number and then tells us if the number is divisible by 2 or by 5
# num = int(input('Enter a number: '))
# is_divisible_by_2 = num % 2 == 0
# is_divisible_by_5 = num % 5 == 0
# print(f"It {is_divisible_by_2 or is_divisible_by_5} that {num} is divisible by either 2 or 5")


# A program that tells if a number is even or not
# num = int(input('Enter a number: '))
# is_even = num % 2 == 0
# print(f"It is {is_even} that {num} is even")

#Using the "not" operator to give admission 
# city = input("Enter your city: ")
# acceptance_status = not(city == 'benin' or city == 'ibadan')
# or write it this way
# acceptance_status = city != 'benin' and city != 'ibadan'
# print(f"CITY ACCEPTANCE STATUS: {acceptance_status}")


# Order of Precedence
#PEMDAS ---> Exponent (**)
# or
#BODMAS


# Membership operators : You are trying to find if something exist in something (they are two of them: in, not in )
# and they give us true or false
# print('a' in 'apple')

# A program that has a long phrase stored somewhere and then asks the user to enter a word that they want to find out whether it exists in the stored phrase. Tell the user whether or not what they searched for can be found in the phrase
# phrase = "to be or not to be found, that is the question"
# searched_word = input('Enter a word to find: ')

# is_found = searched_word in phrase
# print(f"It is {is_found} that '{searched_word}' is found in our phrase.")

# cities = ["lagos", "ibadan", "onitsha", "calabar", "ilisha"]
# print("isha" in cities)
# print("Lagos" in cities[0].capitalize())
# languages = ("spanish", "yoruba", "french", "german")
# print("g" not in languages)

#Write a program that takes a string of colors from the user, seperated by comma. Turn that string of colors to a list. Thne ask the user for their favorite color and then find out if that their favorite color can be found in the list of colors they provided initially.
# string_of_colors = input('Enter list of colors sepearated by commas: ')
# list_of_colors = string_of_colors.split(', ')
# favorite_color = input('Enter favorite color: ')
# found_favorite_color = favorite_color in list_of_colors
# print(found_favorite_color)

# Identity operators: It helps know whether two variables are pointing to the same address in memory.It's not about the values but the address in the memory. (None)



# Bitwise operators
