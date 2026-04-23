# QUESTION 1: Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# sum = 0
# number = input("Enter an integer: ")

# for digit in number:
#         sum += int(digit)

# print("Sum of digits:", sum)


# QUESTION 2: Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts.
# from string import ascii_lowercase

# string = input('Enter something: ').lower()
# vowels = "aeiou"
# consonants = ascii_lowercase.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
# vowels_count = 0
# consonants_count = 0

# for char in string:
#     if char in vowels:
#         vowels_count += 1
#     elif char in consonants:
#         consonants_count += 1

# print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")

#****************OR****************
#  Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7


# text = input("Enter some text: ").lower()

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# for char in text:
#     if not char.isalpha():
#         continue

#     if char in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1

# print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    

# QUESTION 3: Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12.
# number = int(input('Enter a number: '))

# for i in range(1, 13):
#     print(f"number x {i} = {number * i}")

# QUESTION 4: Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# string = input("Enter a string: ")
# reversed_string = ""

# for char in string:
#     reversed_string = char + reversed_string

# print("Reversed string:", reversed_string)

# QUESTION 5: Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# numbers = input("Enter numbers separated by commas: ").split(",")

# new_list = []

# for num in numbers:
#     num = num.strip()
#     if num not in new_list:
#         new_list.append(num)

# print("New list without duplicates:", new_list)

# QUESTION 6:  Write a program that takes an integer input n from the user and prints the first #Fibonacci number is the sum of the previous two.
# 	n numbers in the Fibonacci sequence. Example:
# n = int(input("Enter how many Fibonacci numbers to print: "))

# first = 0
# second = 1

# for i in range(n):
#     print(first, end=" ")
#     next_number = first + second
#     first = second
#     second = next_number
#*******************************OR**************************
#  Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# fibonacci = [0, 1]

# n = int(input("Enter the length of the fibonacci sequence: "))


# for i in range(n-2):
#     next_num = fibonacci[i] + fibonacci[i+1]
#     fibonacci.append(next_num)
#     print(fibonacci)

# print(fibonacci)

# QUESTION 7: Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.


# numbers = input("Enter numbers separated by commas: ").split(",")

# largest = int(numbers[0])

# for num in numbers:
#     num = int(num)
#     if num > largest:
#         largest = num

# print("Largest number:", largest)

# QUESTION 8. Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# n = int(input("Enter an integer: "))
# total = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total += i

# print("Sum of even numbers:", total)

#  QUESTION 9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# text = input("Enter a string: ")
# checked = ""

# for char in text:
#     if char not in checked:
#         count = 0

#         for letter in text:
#             if letter == char:
#                 count += 1

#         print(char, ":", count)
#         checked += char
#************************************OR********************************
#  Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# occurences = {}

# text = input("Enter some text: ")

# for char in text:
#     if char not in occurences:
#         occurences[char] = 1
#     else:
#         occurences[char] += 1


# for char, occurence in occurences.items():
#     print(f"{char}: {occurence}")

# QUESTION 10: Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum.
# n = int(input("Enter an integer: "))

# sum_of_squares = 0

# for i in range(1, n + 1):
#     sum_of_squares += i ** 2

# print("The sum of squares is:", sum_of_squares)

# QUESTION 11: 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. 
# phrase = input("Enter a phrase: ")
# words = phrase.split()
# acronym = ""

# for word in words:
#     acronym += word[0].upper()

# print("Acronym:", acronym)

# QUESTION 12: 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. 
# text = input("Enter a string: ")

# word_count = 0
# in_word = False

# for char in text:
#     if char != " " and in_word == False:
#         word_count += 1
#         in_word = True
#     elif char == " ":
#         in_word = False

# print("Number of words:", word_count)

#***********************OR*************************
# Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# text = input("Enter some text: ")

# no_of_words = 0

# words = text.split()

# print(words)

# for word in words:
#     no_of_words += 1

# print(no_of_words)

# QUESTION 13: 	Collect a string from the user and only print out the words that start with the letter 
# 	‘S’. 
# text = input("Enter a string: ")

# words = text.split()

# for word in words:
#     if word.lower().startswith("s"):
#         print(word)

# QUESTION 14: 	Print all the even numbers from 1 to 20 using the range function and a loop.
# for num in range(2, 21, 2):
#     print(num)

# QUESTION 15: 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.
# numbers = [num for num in range(1, 51) if num % 3 == 0]

# print(numbers)

# QUESTION 16: Go through the string below and if the length of a word is even, print that word.
# st = "Print every word in this sentence that has an even number of letters"

# for word in st.split():
#     if len(word) % 2 == 0:
#         print(word)

# QUESTION 17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
# QUESTION 18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# for i in range(len(names)):
#     print(names[i], grades[i])
    
# QUESTION 19: Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']
# items = ['shoe', 'stick', 'toy', 'fruit']

# for i in range(len(items)):
#     if i % 2 == 0:
#         print(items[i])

# QUESTION 20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# for i in range(len(list1)):
#     if list1[i] != list2[i]:
#         print("Index:", i, "List1:", list1[i], "List2:", list2[i])

#  QUESTION 21. Create a list of the square of each number
# numbers = [1, 2, 3, 4, 5]

# squares = [num ** 2 for num in numbers]

# print(squares)


# # QUESTION 22. Create a list of names that contain the letter 'a'
# names = ["John", "Sara", "Mike", "Amanda"]

# result = [name for name in names if "a" in name.lower()]

# print(result)


# # QUESTION 23. Create a list of Booleans indicating if each number is greater than 10
# numbers = [5, 12, 3, 18, 7]

# result = [num > 10 for num in numbers]

# print(result)


# # QUESTION 24. Create a list of the last characters of each word
# words = ["dog", "cat", "lion", "tiger"]

# last_characters = [word[-1] for word in words]

# print(last_characters)