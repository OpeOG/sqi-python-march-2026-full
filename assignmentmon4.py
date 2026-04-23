# QUESTION 1: Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.
# class NegativeNumberError(Exception):
#     pass
# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError("Number cannot be negative")
#     print("Number is positive.")
# try:
#     number = int(input("Enter a number: "))
#     check_positive(number)
# except NegativeNumberError as e:
#     print(e)
# except ValueError:
#     print("Invalid input")

# QUESTION 2: Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.
# def safe_divide(a, b):
#     try:
#         a = float(a)
#         b = float(b)
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Cannot divide by Zero"
#     except TypeError:
#         return "Input must be numbers"
#     except ValueError:
#         return "Inputs must be convertible to floats"
# a = input("Enter first number: ")
# b = input("Enter second number: ")

# print(safe_divide(a, b))

# QUESTION 3. Read All Lines and Count Them
# ------------------------------------------------------------
# There is a file called "students.txt" with the following content:
#
# Alice
# Bob
# Charlie
# David
# with open("students.txt", "r") as f:
#     lines = f.readlines()
# total_students = len(lines)

# print(f"Total students: {total_students}")

# ------------------------------------------------------------
# QUESTION 4. Convert All Names to Uppercase and Save
# ------------------------------------------------------------
# File: "names.txt"
#
# john
# mary
# peter
#
# Task:
# - Read all names.
# - Convert each name to uppercase.
# - Write them into a new file called "uppercase_names.txt".
#
# After running the program,
# the new file should contain:
#
# JOHN
# MARY
# PETER


# with open("names.txt", "r") as f:
#     contents = f.read()


# with open("uppercase_names.txt", "w") as f:
#     f.write(contents.upper())

# #*****************OR*****************
# with open("names.txt", "r") as f:
#     names = f.read()

# uppercase_names = names.upper()

# with open("uppercase_names.txt", "w") as f:
#     f.write(uppercase_names)

# ------------------------------------------------------------
# QUESTION 5. Remove Empty Lines
# ------------------------------------------------------------
# File: "data.txt"
#
# Apple
#
# Banana
#
# Orange
#
# Task:
# - Read all lines.
# - Remove empty lines.
# - Write the cleaned result into "cleaned_data.txt".
#
# Expected file content:
#
# Apple
# Banana
# Orange
# with open("data.txt", "r") as f:
#     lines = f.readlines()

# with open("cleaned_data.txt", "w") as f:
#     for line in lines:
#         if not line.strip():
#             f.write(line)

# ------------------------------------------------------------
# QUESTION 6. Count Words in File
# ------------------------------------------------------------
# File: "story.txt"
#
# Python is fun
# Coding is powerful
#
# Task:
# - Read the file.
# - Count the total number of words.
# - Print the total.
#
# Sample Execution:
# > python program.py
#
# Expected Output:
# Total words: 6
# with open("story.txt", "r") as f:
#     contents = f.read()
#     words = contents.split()
#     total_words = len(words)
# print(f"The total words is {total_words}")


# ------------------------------------------------------------
# QUESTION 7. Append a New Log Entry
# ------------------------------------------------------------
# File: "log.txt"
#
# System started
#
# Task:
# - Append a new line that says: "User logged in"
#
# Expected file content after running:
#
# System started
# User logged in
# with open("log.txt", "a") as f:
#    f.write("\nUser logged in")


# ------------------------------------------------------------
# QUESTION 8. Reverse Each Line
# ------------------------------------------------------------
# File: "words.txt"
#
# cat
# dog
# fish
#
# Task:
# - Read each line.
# - Reverse the letters.
# - Save results into "reversed_words.txt".
#
# Expected content:
#
# tac
# god
# hsif
# with open("words.txt", "r") as f:
#     lines = f.readlines()

# reversed_lines = [line.strip()[::-1] + "\n" for line in lines]
# reversed_lines = "".join(reversed_lines)

# print(reversed_lines)

# with open("reversed_words.txt", "w") as f:
#     f.write(reversed_lines)

# ------------------------------------------------------------
# QUESTION 9. Add Line Numbers
# ------------------------------------------------------------
# File: "tasks.txt"
#
# Wash dishes
# Do homework
# Clean room
#
# Task:
# - Read the file.
# - Add numbers at the beginning of each line.
# - Save into "numbered_tasks.txt".
#
# Expected content:
#
# 1. Wash dishes
# 2. Do homework
# 3. Clean room
# with open("tasks.txt", "r") as f:
#     lines = f.readlines()
# with open("numbered_tasks.txt", "w") as f:
#     for i, line in enumerate(lines, start=1):
#         f.write(f"{i}. {line}")

# ------------------------------------------------------------
# QUESTION 10. Filter Numbers Greater Than 50
# ------------------------------------------------------------
# File: "numbers.txt"
#
# 12
# 75
# 30
# 88
#
# Task:
# - Read all numbers.
# - Keep only numbers greater than 50.
# - Write them into "big_numbers.txt".
#
# Expected content:
#
# 75
# 88
# with open("numbers.txt", "r") as f:
#     lines = f.readlines()

# with open("big_numbers.txt", "w") as f:
#     for line in lines:
#         number = int(line.strip())
#         if number > 50:
#             f.write(str(number) + "\n")

# ------------------------------------------------------------
# QUESTION 11. Replace a Word
# ------------------------------------------------------------
# File: "message.txt"
#
# I love cats
#
# Task:
# - Replace the word "cats" with "dogs".
# - Save result into "updated_message.txt".
#
# Expected content:
#
# I love dogs
# with open("message.txt", "r") as f:
#     content = f.read()
# updated_content = content.replace("cats", "dogs")

# with open(f"updated_message.txt", "w") as f:
#     f.write(updated_content)


# ------------------------------------------------------------
# QUESTION 12. Merge Two Files
# ------------------------------------------------------------
# File 1: "first.txt"
#
# A
# B
#
# File 2: "second.txt"
#
# C
# D
#
# Task:
# - Read both files.
# - Combine their contents.
# - Write into "merged.txt".
#
# Expected content:
#
# A
# B
# C
# D
# with open("first.txt", "r") as f:
#     content1 = f.read()
# with open("second.txt", "r") as f:
#     content2 = f.read()

# merged_content = content1 + "\n" + content2
# with open("merged.txt", "w") as f:
#     f.write(merged_content)