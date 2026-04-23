# 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# def turn_to_upper(names):
#     return [name.upper() for name in names]
# print(turn_to_upper(['Nelson', 'Opeyemi', 'Winnie', 'Winnifred']))

# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# def get_middle_name(name_dict):
#     return name_dict['middle']
# person = {"first": "Opeyemi", "middle": "Nelson", "last": "Olaoluwa"}
# print(get_middle_name(person))

# **************OR***************************
# def get_middle_name(name_dict: dict[str, str]):
#     if "middle" in name_dict:
#         return name_dict["middle"]
#     return None

# Edge cases -------> These are unusual, extreme, or special situations that can cause problems if you do not handle them properly.
# Happy path -------> This means the normal, correct case where everything works as expected.

# def get_middle_name(name_dict: dict[str, str]):
#     return name_dict.get("middle")


# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))
# print(get_middle_name({}))

# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# def reverse_string(name):
#     return name[::-1]
# print(reverse_string("Nelson"))

# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# def count_vowels(string):
#     return len ([char for char in string if char in 'aeiou'])
# print(count_vowels('nelson'))


# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# def even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]
# print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# def find_max(numbers):
#     return max(numbers)
# print(find_max([17, 51, 63, 26, 10]))

# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# def sum_dict_values(num_dict):
#     return sum(num_dict.values())
# dictionary = {"a": 15, "b": 18, "c": 4}
# print(sum_dict_values(dictionary))

# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# def word_lengths(words):
#     return {word: len(word) for word in words}
# print(word_lengths(["apple", "banana", "cherry"]))

# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# def is_palindrome(string):
#     return string == string[::-1]
# print(is_palindrome('daddy'))

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# def merge_lists(list1, list2):
#     merged = list1 + list2
#     result = []

#     for num in merged:
#         if num not in result:
#             result.append(num)

#     return result

# print(merge_lists([2, 3, 4], [4, 5, 6]))
# ***************OR****************************
# def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
#     return list(set(list1 + list2))
#     return list(set([*list1, *list2]))


# print(merge_lists([1, 2, 3], [3, 4, 5]))


# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# [1, 2, 3, 3, 4, 5]


# flattened_list = [*list1, *list2]
# print(flattened_list)

# 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# If the second number is not provided, it should default to 2.
# def multiply_numbers(a, b=2):
#     return a * b
# print(multiply_numbers(5))
# print(multiply_numbers(5, 3))

# 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# If last_name is not provided, it should only greet with the first name.
# def greet_user(first_name, last_name=""):
#     if last_name == "":
#         return(f"Hello, {first_name}!")
#     else:
#         return(f"Hello, {first_name} {last_name}!")
# print(greet_user("Opeyemi"))
# print(greet_user("Opeyemi", "Nelson"))

# 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# The exponent should default to 2 (square).
# Example 1: power(4) → 16
# Example 2: power(2, 3) → 8
# def power(base, exponent = 2):
#     return base ** exponent
# print(power(4))
# print(power(2, 3))

# 14. Create a function called format_full_name(first, middle="", last="") that returns the full name as a single string.
# If middle or last is not provided, it should still work correctly.
# def format_full_name(first, middle="", last=""):
#     full_name = first

#     if middle != "":
#         full_name += " " + middle

#     if last != "":
#         full_name += " " + last

#     return full_name

# print(format_full_name("Opeyemi", "Nelson", "Olaoluwa"))
# print(format_full_name("Opeyemi", "Olaoluwa"))
# print(format_full_name("Opeyemi"))

# 15. Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying
# a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0
# def calculate_discount(price, discount=10, tax=0):
#     discounted_price = price - (price * discount / 100)
#     final_price = discounted_price + (discounted_price * tax / 100)
#     return final_price

# print(calculate_discount(100))         
# print(calculate_discount(100, 20))     
# print(calculate_discount(100, 20, 5))  

# 16. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     return a + b
# print(sum_numbers(2, 4))

# 17. Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0
# print(is_even(2))
# print(is_even(7))

# 18. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return n > 1

# print(is_prime(10))
# print(is_prime(9))
# print(is_prime(7))
# print(is_prime(2))
# ************************OR*******************************
# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, int(n ** 1/2) + 1):
#         if n % i == 0:
#             return False

#     return True


# print(is_prime(9))

# 19. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return n > 1


# def get_primes_up_to_n():
#     n = int(input("Enter a number: "))
#     primes = []

#     for num in range(2, n + 1):
#         if is_prime(num):
#             primes.append(num)

#     return primes
# print(get_primes_up_to_n())

# ********************OR******************************

# def list_primes(n):

#     pass


# print(list_primes(input("Enter the value of n: ")))


# def list_primes():
#     n = int(input("Enter the value of n: "))
#     primes_up_to_n = []
#     i = 0
#     while True:
        
#         if is_prime(i):
#             primes_up_to_n.append(i)

#         if i == n:
#             break

#         i += 1
#     return primes_up_to_n

# print(list_primes())

# 20. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     return max(a, b)
# print(lesser_of_two_evens(10, 11))

# 21. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# def is_alliteration(two_word_string):
#     words = two_word_string.split()
#     if words[0][0].lower() == words[1][0].lower():
#         return True
#     return False  
# print(is_alliteration('Opeyemi Nelson'))
# print(is_alliteration('Levelheaded llama'))

# 22. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name):
#     return name[:3].capitalize() + name[3:].capitalize()
# print(old_macdonald('macdonald'))

# 23. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# def spy_game(list_of_ints):
#     code = [0, 0, 7]

#     for num in list_of_ints:
#         if num == code[0]:
#             code.pop(0)

#         if len(code) == 0:
#             return True

#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# 24. Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math
# def vol(radius):
#     return (4/3) * math.pi * radius ** 3
# print(vol(3))

# 25. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high):
#     return low <= num <= high
# print(range_check(5, 2, 7))
# print(range_check(5, 15, 16))

# 26. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# def upper_lower(text):
#     num_of_uppercase = 0
#     num_of_lowercase = 0

#     for i in text:
#         if i.isupper():
#             num_of_uppercase += 1
#         elif i.islower():
#             num_of_lowercase += 1

#     return num_of_uppercase, num_of_lowercase
# print(upper_lower('NelSon'))

# 27. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# def unique_list(list_items):
#     new_list = []
#     for i in list_items:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print(unique_list([1, 2, 3, 4, 4, 5, 6, 5]))

# 28. Write a function multiply(list_items) to multiply all the numbers in a list.
# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num
#     return result
# print(multiply([1, 2, 3, 4]))

# 29. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.
# from string import ascii_lowercase
# def is_pangram(text):
#     text = text.lower()
#     for letter in ascii_lowercase:
#         if letter not in text:
#             return False
#     return True

# print(is_pangram("The quick brown fox jumps over the lazy dog")) 
# print(is_pangram("Worthy is the lamb, Hallelujah")) 
#****************************OR******************************
# import string

# def is_pangram(text: str):
#     text = text.lower()
#     alphabets = string.ascii_lowercase
#     # return set(alphabets).issubset(text)
#     return set(alphabets) <= set(text)


# print(is_pangram("The quick brown fox jumps over the lazy dog."))  # True
# print(is_pangram("Pack my box with five dozen liquor jugs."))  # True
# print(is_pangram("The five boxing wizards jump quickly."))  # True
# print(is_pangram("The quick brown fox"))  # False

# 30. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.
# def are_anagrams(s1, s2):
#     return sorted(s1.lower()) == sorted(s2.lower())
# print(are_anagrams("spar", "rasp"))
# print(are_anagrams("car", "cat"))
# print(are_anagrams("Silent", "listen"))

# 31. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# print(calculate_bmi(70, 2.89))

# 32. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).
# def calculate_simple_interest(principal, rate, time):
#     simple_interest = (principal * rate * time) / 100
#     return simple_interest
# print(calculate_simple_interest(100, 5, 2))
