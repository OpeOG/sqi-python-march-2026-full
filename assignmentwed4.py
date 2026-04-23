# * QUESTION 1: Collect two numbers as input from the user and assign as variables, a and b, write an if statement that prints "a and b are both positive" if both a and b are positive, prints "Only one is positive" if one of them is positive, and prints "Neither is positive" if neither is positive.
# a = int(input('Enter any number: '))
# b = int(input('Enter any number: '))
# if a > 0 and b > 0:
#     print("both a and b are positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")

# * QUESTION 2: Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# Collect comma-separated input
# user_input = input("Enter three numbers separated by comma: ").split(', ')
# x, y, z = user_input
# x = float(user_input[0])
# y = float(user_input[1])
# z = float(user_input[2])

# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")

# * QUESTION 3: You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# x = int(input('Enter a number: '))
# y = int(input('Enter a number: '))
# z = int(input('Enter a number: '))
# if x == y or x == z or y == z:
#     print("Two are equal")
# else:
#     print("All different or All same")

# * QUESTION 4: You have two variables, status1 and status2, provided through user input, each of which can be "active", “inactive", or "pending". Write an if statement to print "Both active" if both statuses are "active", "One active" if exactly one is "active", and "None active" if neither is "active".
# status1 = input('Enter a status: ')
# status2 = input('Enter a status: ')

# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print('one is active')
# else:
#     print('None active')

# * QUESTION 5: You have a variable access_level provided through user input which can be "admin", "user", or "guest". Write an if statement that prints "Full access" if access_level is "admin", "Limited access" if it is "user", and "No access" if it is "guest".
# access_level = input(('Enter an access level: ')).lower()
# if access_level == 'admin':
#     print("Full access")
# elif access_level == 'user':
#     print("Limited access")
# elif access_level == 'guest':
#     print("No access")
# else:
#     print("Nothing for you")

# * QUESTION 6: Write a program that takes three numbers (num1, num2, num3) as a comma-separated string input from the user and prints the greatest number. Use conditional statements to determine which number is the greatest. Bonus point if you can do it without else statements.

# user_input = input("Enter three numbers separated by comma: ")

# parts = user_input.split(',')

# num1 = float(parts[0])
# num2 = float(parts[1])
# num3 = float(parts[2])

# if num1 >= num2 and num1 >= num3:
#     print("Greatest number is:", num1)

# if num2 >= num1 and num2 >= num3:
#     print("Greatest number is:", num2)

# if num3 >= num1 and num3 >= num2:
#     print("Greatest number is:", num3)


# QUESTION 7: * Have user details stored in user = {"username": "admin123", "password": "pass123"}. Then write a program that asks a user to provide their user name and password. If it matches the details in that user dictionary, then say "Login Successful". Otherwise, "Invalid login"
# entered_username = input('Enter username: ')
# entered_password = input('Enter password: ')
# user = {"username": "admin123", "password": "pass123"} 
# if entered_username == user["username"] and entered_password == user["password"]:
#     print("Login Successful")
# else:
#     print("Invalid Login")

# * QUESTION 8: Write a program that takes a number and tells if the number is even or odd.
# num = int(input('Enter a number: '))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

# * QUESTION 9: Write a program that takes a number and tell if that number is a multiple of 12
# num = int(input('Enter a number: '))
# if num % 12 == 0:
#     print('The number is a multiple of 12')
# else:
#     print('The number is not a multiple of 12.')

# * QUESTION 10: A shop is running a discount system for its customers. A user enters the total price of an item and a discount code. If the user enters the code "SAVE10", they get a 10% discount on the price. If they enter "SAVE20", they get a 20% discount. If the code entered is "VIP", the program should first check the price: if the price is greater than 4000, the user gets a 30% discount, otherwise they get a 15% discount. If the user enters any other code, no discount should be applied and the full price should be used. Write a Python program using only if and nested if statements (no loops) to calculate and display the final price after applying the appropriate discount

# price = float(input('Enter total price: '))
# discount_code = input('Enter discount code: ')

# if discount_code == "SAVE10":
#     discount_amount = (0.1 * price)
# elif discount_code == "SAVE20":
#     discount_amount = (0.2 * price)
# elif discount_code == "VIP":
#     if price > 4000:
#         discount_amount = (0.3 * price)
#     else:
#         discount_amount = (0.15 * price)
# else:
#     discount_amount = 0
#     print("No discount applied")
# total_amount_to_pay = price - discount_amount
# print(f" Your total amount (after discount): {price - discount_amount}")

# * A school is building a simple grading system. A student enters their exam score and whether they submitted their assignment (True or False). If the score is 70 or above, the student passes, but the program should then check if the assignment was submitted: if it was, the student gets a "Distinction", otherwise they get just a "Pass". If the score is between 50 and 69, the student also passes, but if they did not submit the assignment, they should be given a "Carryover", otherwise they get a normal "Pass". If the score is below 50, the student fails, but if they submitted the assignment, the program should display "Fail but eligible for review", otherwise just "Fail". Write a Python program using only if and nested if statements (no loops) to determine and display the student’s final result.
# exam_score = int(input('Enter exam score: '))
# submission_status = input('Did you submit your assigment? (True/False): ')

# if exam_score >= 70:
#     if submission_status == 'True':
#         print("Distinction")
#     else:
#         print("Pass")
# elif exam_score >= 50 and exam_score <= 69:
#     if submission_status == 'True':
#         print("Pass")
#     else:
#         print("Carryover")
# elif exam_score < 50:
#     if submission_status == 'True':
#         print("Fail but eligible for review")
#     else:
#         print("Fail")