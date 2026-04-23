# * QUESTION 1: Write a program that uses a while loop to print numbers from 1 to 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# * QUESTION 2: Write a program that takes an integer n from the user and calculates the sum of all natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# n = int(input('Enter a number: '))
# sum_total = 0
# i = 1
# numbers_list = []
# while i <= n:
#     sum_total += i
#     numbers_list.append(str(i))
#     i += 1

# print(sum_total)
# all_numbers_joined = ' + '.join(numbers_list)
# print(f"{all_numbers_joined} ({sum_total})")


# * QUESTION 3: Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.
# from random import randint
# secret = randint(1, 50)


# i = 1
# while i <= 5:
#     user_guess = int(input('Guess a number: '))
#     if user_guess == secret:
#         print('You win!') 
#         break   
#     elif user_guess > secret:
#         print("Too high")
#     elif user_guess < secret:
#         print('Too low')
       
#     i += 1
# print(f'The right guess is: {secret}')


# * QUESTION 4: Write a program that keeps asking the user for a password until they enter the correct one. The correct password is secret.
# password = input("Enter password: ")

# while password != "secret":
#     password = input("Enter password: ")

# print("Access granted")

#  ***********************OR************************************

# while True:
#     password = input("Enter password: ")
#     if password == 'secret':
#         print('Correct password')
#         break
#     else:
#         print('Incorrect password')

# * QUESTION 5: Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# from time import sleep
# from random import randint
# user_input = int(input('Enter a number: '))
# i = user_input
# while i >= 0:
#     delay = randint(1, 8)
#     sleep(delay)
#     print(i)
#     i -= 1


# * QUESTION 6: Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input('Enter any number: '))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# * QUESTION 7: Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# user_input = input('Enter a string: ')
# vowels = 'aeiou'
# vowels_count = 0
# i = 0
# while i < len(user_input):
#     if user_input[i] in vowels:
#         vowels_count += 1
#     i += 1
# print("The total count of vowels is: ",vowels_count)

# * QUESTION 8: Write a program that takes a string input from the user and uses a while loop to reverse the string. Do not use slicing or reversed().
# user_input = input('Enter a string: ')
# index = len(user_input) -1 
# reversed_text = ''
# while index >= 0:
#     reversed_text += user_input[index]
#     index -= 1
# print("Reversed string:", reversed_text)

# Or

# my_input = input('Enter a string: ')

# i = len(my_input) -1 # ---->start counting from the length of the input # Tell us how many times the loop has run and also your value will be used as an index on our input

# while i >= 0: # this means until you get to zero keep reducing that's why it is i >= 0

#     print(my_input[i])
#     i -= 1

# * QUESTION 9: Write a program that takes comma-separated integers from the user, converts that to a tuple and uses a while loop to find the minimum value in the tuple. Do not Use the min() function.
# user_input = input("Enter integers separated by commas: ")
# numbers_list = user_input.split(',')
# conversion_to_tuple = tuple(int(num) for num in user_input.split(','))
# minimum = conversion_to_tuple[0]
# i = 0
# while i < len(conversion_to_tuple):
#     if conversion_to_tuple[i] < minimum:
#         minimum = conversion_to_tuple[i]
#     i += 1
# print("Minimum value:", minimum)

# OR 
# comma_separated_numbers = int(input("Enter numbers separated ny comma: "))

# numbers = (23, 5, 34, 56, 78, 98, 19, 10, 4, 6, 3, 5, 4)
 # First of all, we assume the first value is the minimum then we check it against the other numbers. So run a loop from the index 0 which we believe is the minimum to the length of numbers. We are not making use of an input yet like the assignment stated. So let's just make use of this random numbers.

# print(min(numbers)) # we are not to use the min() function though so we go the right way according to the question
# lowest_num = numbers[0] # we assume the lowest number is always at the index 0
# i = 0
# while i < len(numbers): # this means while 0 is less than the numbers, which we use len(numbers) to find out the total characters of the number
    # if numbers[i] < lowest_num: # this means if the number at the current counter[i] which changes as the loop runs btw is lesser than "lowest_num which is the number at index[0] since we believe the lowest number is at index 0 and we earlier created a value for it. Equate the now believed lowest number to 'numbers[i]', which means 'numbers[i]' is now the lowest number."
        # lowest_num = numbers[i] # The lowest number is now stored in (numbers[i]. This keeps changing as this loop runs)

    # i += 1
# print("The lowest number: ", lowest_num)

# * QUESTION 10: Write a program that takes a string input from the user and uses a while loop to count the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}
# user_input = input('Enter a string: ')
# character_count = {}
# i = 0
# while i < len(user_input):
#     char = user_input[i]

#     if char in character_count:
#         character_count[char] += 1
#     else:
#         character_count[char] = 1

#     i += 1

# print("Character counts:", character_count)

#*************************OR*********************************
# Write a program that takes a string input from the user and uses a while loop to count the occurrences of each character, storing the counts in a dictionary.
# string = input("Enter a string: ")
# unique_chars= list(set(string)) #  Take the string and turn it to a set so we can remove duplicate characters( since we are looking for unique characters and only set let you achieve that) and then turn it to a list so we can do indexing on it(since you can't do indexing on a set and we need ). So we can have unique characters.
# i = 0 # we start counting at index[0]
# chars_and_frequencies = {} # we create an empty dictionary so we can add our values
# while i < len(unique_chars): 
#     current_unique_char = unique_chars[i]
#     print(f"{current_unique_char} -> {string.count(current_unique_char)}")
#     chars_and_frequencies[current_unique_char] = string.count(current_unique_char)
#     i += 1
# print(chars_and_frequencies)

# * QUESTION 11: Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# user_input = input('Enter a string: ')
# vowels = "aeiou" # we store the vowels in a variable so we can always check against it.
# vowels_count = 0 
 # we used vowel count since we are counting the number of vowels, so it will be nice to have that stored in a variable and then start counting from 0 since it doesn't have an existing an value
# consonants_count = 0 
# we used consonant count since we are counting the number of consonant, so it will be nice to have that stored in a variable and then start counting from 0 since it doesn't have an existing an value

# i = 0
# while i < len(user_input):
#     if user_input[i] in vowels:
#         vowels_count += 1
#     else: 
#         consonants_count += 1
#     i += 1
# print("Number of vowels and consonants found are: ", vowels_count, consonants_count)

# *************OR*************
# from string import ascii_lowercase
# string = input('Enter something: ').lower()
# vowels = "aeiou"
# consonants = ascii_lowercase.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '') # ascii_lowercase will give us all the alphabets in lowercase but since we have our vowels stored in a variable already and we only need the consonants, you now have to replace the vowels with empty strings. Whcih means we'll be left with only consonants at the end of the day.
# vowels_count = 0
# consonants_count = 0

# i = 0
# while i < len(string):
#     if string[i] in vowels:
#         vowels_count += 1
#     elif string[i] in consonants:
#         consonants_count += 1
#     i += 1
# print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")



# QUESTION 12: Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# user_balance = float(input('Enter your balance: ')) # this is placed outside the loop because we don't want the balance to keep resetting since we were told the user shouldn't withdraw more than their balance, so putting in the loop won't let us the exact balance after the user makes a withdrawal since it would have been resetted.

# while True:
#     withdrawal_amount = float(input('Enter the amount you want to withdraw: '))
#     if withdrawal_amount > user_balance:
#         print("Insufficient balance")
#     else:
#         user_balance -= withdrawal_amount  
#         print("Withdrawal successful.")
#         print("Remaining balance:", user_balance)

#     choice = input("Do you want to make another withdrawal? (yes/no): ")

#     if choice.lower() != "yes":
#         break

# print("Transaction ended.")
# print("Final balance:", user_balance)

# QUESTION 13: Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# total_cost = 0 # we save this in a variable since we need total cost and of course it will start from 0

# while True:
#     price = float(input("Enter item price: "))

#     if price < 0:
#         print("Price cannot be negative.")
#     else:
#         total_cost += price

#     choice = input("Do you want to add another item? (yes/no): ")

#     if choice.lower() != "yes":
#         break

# print("Total cost:", total_cost)


# QUESTION 14: Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# while True:
#     user_input = input('Enter a password: ')

#     if len(user_input) >= 8 and len(user_input) <= 25:
#         print("Password Accepted")
#         break
#     else:
        # ("Password not Accepted")  # Ask chat if i want it to print "Password not accepted" and then proceed to tell the user to input another password  not just asking them straightup to input another password after inputting the wrong password.




# QUESTION 15: Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.
# while True:
#     user_age = int(input('Enter your age: '))
#     if user_age >= 0:
#         print("Age Accepted")
#         break   # you use 'break' only in loops
#     else:
#         print("Invalid age. Please enter a valid age.")  

#  QUESTION 16: Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit
# * QUESTION: Write a program that tracks the inventory of items in a store.
# The user should be able to add or remove items and the program should display
# the current inventory after each operation. The program stops when the user
# decides to exit.
# The current store inventory is {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

# while True:
#     print("Current inventory:", inventory)
#     operation = input("Enter operation (add, remove, exit): ").lower()

#     if operation == "add":
#         item = input("Enter item name to add: ").lower()
#         quantity = int(input("Enter quantity to add: "))

#         if item in inventory:
#             inventory[item] += quantity
#         else:
#             inventory[item] = quantity

#         print("Updated inventory:", inventory)

#     elif operation == "remove":
#         item = input("Enter item name to remove: ").lower()
#         quantity = int(input("Enter quantity to remove: "))

#         if item in inventory:
#             if quantity <= inventory[item]:
#                 inventory[item] -= quantity

#                 if inventory[item] == 0:
#                     del inventory[item]

#                 print("Updated inventory:", inventory)
#             else:
#                 print("Not enough stock to remove.")
#         else:
#             print("Item not found in inventory.")

#     elif operation == "exit":
#         print("Exiting program.")
#         break

#     else:
#         print("Invalid operation. Please enter add, remove, or exit.")


# *************OR***************************
# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}
# print("*************YOUR INVENTORY*******************")
# print(inventory)
# while True:
#     option = input('Choose an action (add, remove, show, exit): ')

#     if option not in ['add', 'remove', 'show', 'exit']:
#         print("Invalid option")
#         continue

#     if option == 'add' or option == 'a':
#         item_name = input("Enter item name: ")
#         item_qty = int(input("Enter item qty: "))

#         # If the item name supplied already exists in our inventory above
#         if item_name in inventory:
#             inventory[item_name] += item_qty
#         else:
#             # If it does not already exist, add it as a new item into our inventory
#             inventory[item_name] = item_qty

#     elif option == 'remove' or option == 'r':
#         item_name = input ("Enter item name: ")
#         if item_name not in inventory:
#             print(f"{item_name} not an item in your inventory")
#             print("Your inventory contains: ", inventory)
#             continue
    
#         del inventory[item_name]
#         print(inventory)
    
#     elif option == 'show':
#         print(inventory)
#     else:
#         print('Exiting inventory')
#         break


# Multiplication Table 3
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

# i = 1
# while i <= 12:
#     print(f" 6 x {i} = {6 * i}")
#     i += 1

# A program that asks the user to input a number, then do a multipliaction table for that number.
# user_input = int(input('Enter a number: '))
# i = 1
# while i <= 12:
#     print(f" {user_input} x {i} = {user_input * i}")
#     i += 1

