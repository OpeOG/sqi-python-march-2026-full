# QUESTION 1: Write a program that asks the user for their first name and birth year, then creates a username using the first three letters of their name and the last two digits of their birth year.
# user_first_name = input('Enter first name: ')
# user_birth_year = input('Enter birth year: ')
# first_three_letters_user_name = user_first_name[:3]
# last_two_digits_userbirthyear = user_birth_year[-2:]
# username = first_three_letters_user_name + last_two_digits_userbirthyear
# print(username)

# QUESTION 2: Write a program that asks the user to enter a sentence and prints the sentence in uppercase and also replaces all spaces with hyphens
# user_sentence = input('Enter a sentence: ')
# new_sentence = user_sentence.upper().replace(' ', '-')
# print(new_sentence)

#QUESTION 3: Ask the user to enter their full name and print the initials of the name in uppercase.
# user_fullname = input('Enter fullname: ')
# initials_fullname = user_fullname.split()

# print(initials_fullname[0][0])

# QUESTION 4: Write a program that asks the user to enter two numbers and prints the sum, difference, product, and quotient (division) of the two numbers.
# user_number_1 = float(input('Enter number : '))
# user_number_2 = float(input('Enter number : '))
# sum = user_number_1 + user_number_2
# difference = user_number_1 - user_number_2
# product = user_number_1 * user_number_2
# quotient = user_number_1 / user_number_2
# print(sum)
# print(difference)
# print(product)
# print(quotient)

# QUESTION 5: Write a program that asks the user to enter a number and prints the square and cube of that number.
# user_number = float(input('Enter a number: '))
# square_of_usernumber = user_number ** 2
# cube_of_usernumber = user_number ** 3
# print(square_of_usernumber)
# print(cube_of_usernumber)



# QUESTION 6: Ask the user to enter the length and width of a rectangle and calculate the area and perimeter.
# length_of_rectangle = float(input('Enter the length of a rectangle: '))
# width_of_rectangle = float(input('Enter the width of a rectangle: '))
# area_of_rectangle = length_of_rectangle * width_of_rectangle
# perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
# print(area_of_rectangle)
# print(perimeter_of_rectangle)

# QUESTION 7: Write a program that asks the user to enter the price of an item and the quantity bought, then calculate the total cost.
# price_of_item = float(input('Enter price: '))
# quantity_bought = int(input('Enter quantity bought: '))
# total_cost = price_of_item * quantity_bought
# print(total_cost)

# QUESTION 8: Ask the user to enter three numbers and print the average of the numbers.
# first_number = int(input('Enter number: '))
# second_number = int(input('Enter number: '))
# third_number = int(input('Enter number: '))
# average = (first_number + second_number + third_number) / 3
# print(average)

# QUESTION 9: 
# * Ask the user to enter their email address and check whether the character "@" is in the email.
# email_address = input('Enter email address: ')
# valid = "@" in email_address
# print(valid)

# QUESTION 10: Write a program that asks the user to enter a password and checks whether the character "#" is in the password.
# user_password = input('Enter password: ')
# valid_password = "#" in user_password
# print(valid_password)

# QUESTION 11: Ask the user to enter a word and check whether the letter "a" appears anywhere except the first character.
# user_word = input('Enter a word: ')
# valid_word = "a" in user_word[1:]
# print(valid_word)

# QUESTION 12: Write a program that asks the user to enter a word and checks whether the last letter of the word appears somewhere else inside the word.
# user_word = input('Enter a word: ')
# last_letter = user_word[-1]
# valid_word = last_letter in user_word[:-1]
# print(valid_word)

# QUESTION 13: Write a program that asks the user to enter a word and checks whether the word contains any vowel (a, e, i, o, u). Hint; Logical
# user_word = input('Enter word: ')
# valid_word = "a" in user_word or "e" in user_word or "i" in user_word or "o" in user_word or "u" in user_word
# print(valid_word)

# QUESTION 14: 
# * Write a program that takes a number and tell whether or not the number is positive. (More than 0)
# user_number = int(input('Enter number: '))
# is_positive = user_number > 0
# print(is_positive)

# QUESTION 15: Write a program that asks the user to enter a word and check whether the word contains both "a" and "e" but does not contain "i".
# user_word = input('Enter a word: ')
# valid_user_word = "a" in user_word and "e" in user_word and "i" not in user_word
# print(valid_user_word)