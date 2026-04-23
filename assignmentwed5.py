#  QUESTION 1: Is there any email address that contains ".org"?
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# any_amails_contains_org = any("org" in email for email in emails)
# print(any_amails_contains_org)

# # QUESTION 2: Are all numbers odd?
# values = [1, 3, 5, 7, 9]
# all_numbers_odd = all (value for value in values if value % 2 != 0)
# print(all_numbers_odd)


# # QUESTION 3: Are all words longer than 2 characters?
# words = ["hi", "dog", "go", "sun"]
# all_words_longer_than_2chars = all(len(word) > 2 for word in words)
# print(all_words_longer_than_2chars)

# QUESTION 4: Create a list of triple the value of each number
# nums = [2, 4, 6, 8]
# triple_of_each_number = [num * 3 for num in nums]
# print(triple_of_each_number)

# # QUESTION 5: Are all temperatures above 0°C?
# temperatures = [12, 7, 3, -1, 5]
# all_temperatures_above_0degrees = all(temperature > 0 for temperature in temperatures)
# print(all_temperatures_above_0degrees)

# # QUESTION 6: Do all words end with a vowel?
# fruits = ["banana", "mango", "kiwi", "grape"]
# all_words_end_with_vowel = all(fruit.lower().endswith(('a', 'e', 'i', 'o', 'u')) for fruit in fruits)
# print(all_words_end_with_vowel)

# # QUESTION 7: Create a list of words in lowercase
# greetings = ["HELLO", "WORLD", "PYTHON"]
# words_in_lowercase = [greeting.lower() for greeting in greetings]
# print(words_in_lowercase)

#  QUESTION 8: Is there any number less than 0?
# numbers = [5, 4, 3, 3, 8]
# numbers_less_than_0 = any(number < 0 for number in numbers)
# print(numbers_less_than_0)

# # QUESTION 9: Create a list of words that contain the letter 'e'
# items = ["sky", "tree", "rock", "stone"]
# contains_letter_e = ['e' in item for item in items]
# print(contains_letter_e)

# # QUESTION 10: Are all names starting with uppercase letters?
# names = ["Alice", "Bob", "charlie", "David"]
# all_names_start_uppercase = all(name[0].isupper() for name in names)
# print(all_names_start_uppercase)

# # QUESTION 11: Is there any sentence longer than 20 characters?
# sentences = ["Short one", "This is a much longer sentence", "Okay"]
# sentence_longer_than_20chars = any(len(sentence) > 20 for sentence in sentences)
# print(sentence_longer_than_20chars)

# QUESTION 12:
#  Scenario: You need to check if a user's password is strong enough.
# # Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:
# # Is at least 8 characters long.
# # Contains both uppercase and lowercase characters.
# # Contains at least one digit.
# # Contains at least one special character (e.g., !@#$%^&*()).
# # Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False. 
# # DO NOT USE REGEX.

# user = input('Enter a password: ')
# is_at_least_8chars_long = len(user) >= 8
# print(is_at_least_8chars_long)

# has_upper = any(char.isupper() for char in user)
# has_lower = any(char.islower() for char in user)
# contains_both_uppercase_and_lowercase = has_upper and has_lower
# print(contains_both_uppercase_and_lowercase)

# contains_at_least_one_digit = any(char.isdigit() for char in user)
# print(contains_at_least_one_digit)

# contains_at_least_one_special_character = any(not char.isalnum() for char in user)
# print(contains_at_least_one_special_character)

# strong_password = (
#     is_at_least_8chars_long
#     and contains_both_uppercase_and_lowercase
#     and contains_at_least_one_digit
#     and contains_at_least_one_special_character
# )
# print(f"It is {strong_password} that the user's password is strong enough")

