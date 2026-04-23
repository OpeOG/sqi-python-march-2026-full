# when the function greet() is called, the program's control transfers to the function definition.
# All the code inside the function is executed.
# The control of the program jumps to the next statement after the function call.

# DRY - Don't Repeat Yourself


# Using function for the assignment given
# A strong password:
# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# def is_strong_password(password):
#     has_at_least_8_chars = len(password) >= 8

#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special_char = False

#     special_chars = "!@#$%^&*()"

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_chars:
#             has_special_char = True

#     print(all([has_upper, has_lower, has_digit, has_special_char, has_at_least_8_chars]))

# is_strong_password("Passw0rd!")
# is_strong_password("p@$$W0rd!")
# is_strong_password("12345678")


# def greet():
#     print("Hello, and good morning! ☀️")


# greet()

# def greet_v2(name):
#     print(f"Hello, and good morning {name}! 👋")

# greet_v2("Ope")
# greet_v2("Dele")
# greet_v2("Winnie")
# greet_v2("Tobi")


# def square(num):
#     print(num ** 2)

# square(6)
# square(4)
# square(3)
# square(7)
# square(9)

# def add_two_nums(num1, num2):
#     print(num1 + num2)
# add_two_nums(8, 4)


# Create a function called 'sing' that takes in nothing and print "I am singing"
# def sing():
#     print("I am singing")
# sing()

# # Create a function called 'person_sings' that takes a string 'name' and prints "{name}" is singing
# def person_sings(name):
#     print(f"{name} is singing")
# person_sings("Nelson")

# #  Create a function called 'perform_duet' that takes in 2 strings'person1' and 'person2' and prints "{person1}"
# def perform_duet(person1, person2):
#     print(f"{person1} and {person2}")
# perform_duet("Nelson","Opeyemi")

# # Create a function called 'perform_harmony' that takes in a list called 'people' and prints out each person
# def perform_harmony(people):
#     for person in people:
#         print(f"{person} is singing")
# perform_harmony(["Winnie", "Tobi", "Ope", "Dele"])

# print("Lorem ipsum dolor")  # 1

# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8




# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12

# def add_two_numbers_return(first_num, second_num):
#     return (first_num + second_num)
# print(add_two_numbers_return(5, 2))
# sum_of_nums = add_two_numbers_return(2, 8)
# print(sum_of_nums)

# def add_two_numbers_print(first_num, second_num):
#     print(first_num + second_num)


# add_two_numbers_print(4, 7)


# upper_name = "James".upper()

# print(upper_name)

# def add_two_numbers_return(first_num, second_num):
#     return first_num + second_num



# result = add_two_numbers_return(5, 8)
# print(result)

# print(add_two_numbers_return(5, 8))



# def upper_and_lower(name):
#     return name.upper(), name.lower()

# # result = upper_and_lower("Kenneth")

# # print(result)

# upper, lower = upper_and_lower("Kenneth")

# print(upper)
# print(lower)


# my_list = [1, 2, 3]
# my_list.append(4)
# popped = my_list.pop(1)
# print(popped)

# print(my_list)

# def add_two_numbers_return(first_num, second_num):
#     print(first_num + second_num)


# add_two_numbers_return(5, 2)


# def add_two_numbers_return(first_num, second_num):
#     return (first_num + second_num)


# print(add_two_numbers_return(5, 2))

# sum_of_nums = add_two_numbers_return(2, 8)

# print(sum_of_nums)


# Write a function called "raise to power" that takes in "base" and "exponent" and returns base raised to the power of exponent
# Sample execution:
# print(raise_to_power(4,3))
# 64


# def raise_to_power(base, exponent):
#     return base ** exponent
# result = raise_to_power(4, 3)
# print(result) 

# def upper_and_lower(name: str):
#     return name.upper(), name.lower()


# print(upper_and_lower("James"))

# type hint or annotation


# def show_name_with_len(names_with_lens: list[tuple[str, int]]):
#     # for name, len in names_with_lens:
#     #     print(f"{name} -> {len}")

#     for item in names_with_lens:
#         name, len = item
#         print(f"{name} -> {len}")


# names_with_their_lens = [("James", 5), ("John", 4), ("Kenneth", 7)]
# show_name_with_len(names_with_their_lens)

# books: list[dict[str, str | int]] = [
#     {"title": "And then there were None", "year_published": 2022},
#     {"title": "The Silent Patient", "year_published": 2002},
#     {"title": "Things Fall Apart", "year_published": 1998},
#     {"title": "The Concubine", "year_published": 1902},
# ]

# Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0
# print(is_even(7))  
# print(is_even(2))  

# OR
# def is_even(n: int):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(5))
# print(is_even(6))


# def is_even(n: int):
#     if n % 2 == 0:
#         return True
#     return False
    
# print(is_even(5))
# print(is_even(6))

# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False
# def is_alliteration(two_word_string):
#     words = two_word_string.split()
#     return words[0][0].lower() == words[1][0].lower()
# print(is_alliteration("Opeyemi Nelson"))  
# print(is_alliteration("Tobi Dada"))  


# Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# def turn_to_upper(names):
#     names_in_uppercase = []
#     for name in names:
#         names_in_uppercase.append(name.upper())
#     return names_in_uppercase
# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))

 # ************ USING LIST COMPREHENSION APPROACH TO SOLVE SAME QUESTION *****************
# def turn_to_upper(names):
#     return [name.upper() for name in names]
# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))


# def greet(name):
#     print(f"Hello,{name} good morning, how are you doing today?.")
# greet('Opeyemi')

# ******************************* SELF WORK ********************************

# def greet():
#     print("Hello, World!") # this wont't be printed the function has been commented on
#     print("This should print first") # this wont't be printed the function has been commented on
# print("This will only print when we call greet since it's indented under it, or betterstill move it out and it will be printed whether you call the function or not") #1
# # greet()
# print("Outside Function") #2
# print("This will print no matter what happens, whether you call out the greet function or not since it's not indented under the greet function") #3

# def add_numbers(num1, num2):
#     multiplication_of_numbers = num1 * num2
#     print(multiplication_of_numbers)
# add_numbers(4, 5)
# ******************************* SELF WORK ********************************

# for i in range(3):
#     num = eval(input('Enter a number: '))
#     print ('The square of your number is', num*num)
# print('The loop is now done.')

# **************************************** QUICK WORK ****************************************************
# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.
# Hint: * in a function means collect many arguments in a tuple
# Test Data:
# def get_total_length(*words):
#     total = 0
#     for word in words:
#         total += len(word)
#     return total
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

#*************************** OR ******************************
# def get_total_length(*words):
#     total = 0
#     return sum(len(word) for word in words)

# print(get_total_length("apple", "banana", "car"))   
# print(get_total_length("hi", "hello")) 
          
    
# 2. Create a function called highest_score that returns the name of the student with the highest score.

# def highest_score(**students):
#     highest_name = ""
#     highest_mark = 0

#     for name, score in students.items():
#         if score > highest_mark:
#             highest_mark = score
#             highest_name = name

#     return highest_name
# print(highest_score(Ope=72, Winnie=89, Tobi=67))   
# print(highest_score(Winnifred=90, Tobi=91, Nelson=88)) 
#************************************* QUICK WORK *******************************************


# -------------------------------------*ARGS AND **KWARGS-------------------------------------*
# * is for many positional arguments and gives a tuple
# ** is for many keyword arguments and gives a dictionary
# Very simple table in words

# *args
# many plain values
# no labels
# stored as tuple

# **kwargs
# many named values
# each has a label
# stored as dictionary


# def greet_everyone(names: list):
#     for name in names:
#         print(f"Heyyy, {name}")

    
# greet_everyone(["Kemi", "Favour", "Tina", "Matilda"])

# This won't throw an error because this function is not receiving many separate arguments. It is receiving one single argument, and that one argument is a list, the loop then goes through the list. But if you want the function to receive many arguments, you can then make use of the *args(is used when you want to pass many separate values into a function.)

# def greet_everyone(*names):
#     for name in names:
#         print(f"Heyyy, {name}")

# greet_everyone()
# greet_everyone("Kemi")
# greet_everyone("Kemi", "Favour", "Tina", "Matilda")

# print("ebjnfk",'efbnjkmd,l2;.s1/',"yeguifo,d.", 7, True, None, sep=":")# this means the arguments will be seperated by what you have in the seperators, but if you don't have a seperator, pyhton will seperate it with space by default
# print()

# def greet_everyone_with_emojis(**names_with_emojis):
#     for name, emoji in names_with_emojis.items():
#         print(f"{name} {emoji}")

# greet_everyone_with_emojis()
# greet_everyone_with_emojis(winnie="😀")
# greet_everyone_with_emojis(winnie="😀", ope="😩", tobi="🤗")

# or betterstill, save it in a variable, then print it the with the function as seen below
# names_with_emojis = {'winnie Igboama': '😀', 'ope': '😩', 'tobi': '🤗'}
# greet_everyone_with_emojis(**names_with_emojis)

# -------------------------------------*ARGS AND **KWARGS-------------------------------------*



# *-------------------------------------RECURSION-------------------------------------*
# Note: Recursion is when a function calls itself.

# def power(base, exponent):
#     if exponent == 0:  # Base case ---> This is the stopping point. Without it, the function will keep calling itself forever
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call
    

# print(power(2, 998))  # Output: 8

# 2 * power(2, 2)

# 2 * 2 * power(2, 1)

# 2 * 2 * 2 * power(2, 0)

# 2 * 2 * 2 * 1 = 8


# import random


# account_numbers = [2, 7]

# def generate_account_number():
#     account_number = random.randint(1, 10)
#     if account_number in account_numbers:
#         print(f"{account_number} is already taken")
#         return generate_account_number()
#     print(f"Account number generated: {account_number}")
#     account_numbers.append(account_number)
#     return account_number

# while True:
#     generate_account_number()
#     stop = input("Enter 'x' to stop or leave blanl to continue: ").strip().lower()

#     if stop == "x":
#         print("Exiting")
#         break


# *-------------------------------------RECURSION-------------------------------------*



# *-------------------------------------SCOPE-------------------------------------*
# Note: Where a variable can be seen or used in your program. We have global scope and a local scope.
# Global Scope -----> A variable in global scope is created outside a function.
# global_var = 12   -----> This is a global variable because it is outside the function. That means it can usually be accessed from many parts of the program.
# Local Scope -----> A variable in local scope is created inside a function.
# def my_function():
#     local_var = 10  # Local scope
#     print(local_var)
#     global global_var # “Inside this function, I want to work with the global variable called global_var, not    create a new local one.”Without this line, Python would treat an assignment like global_var = 20
# as a new local variable.
#     global_var = 20
#     print("Printing from inside the function: ", global_var)

# my_function()
# print("Printing from outside the function", global_var)

# *-------------------------------------SCOPE-------------------------------------*



# *-------------------------------------DOCSTRINGS-------------------------------------*

# docstrings - documentation strings
# comment = normal note for humans
# docstring = documentation note for humans and Python tools
# def add_two_nums(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
#     return a + b
# print(add_two_nums(4, 7))
# print(add_two_nums.__doc__)

# *-------------------------------------DOCSTRINGS-------------------------------------*

