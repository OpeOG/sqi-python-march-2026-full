# * QUESTION 1: Write a program that reads a string called palindrome supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palindrome = input("Enter word: ").lower().replace(" ", '')

# if palindrome == palindrome[::-1]:
#     print("Is a palindrome")
# else:
#     print("Is not palindrome")

# * QUESTION 2: Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = float(input("Enter degree: "))
# angle2 = float(input("Enter degree: "))
# angle3 = float(input("Enter degree: "))

# if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# * QUESTION 3: You have a single character variable ch supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# ch = input("Enter word: ").lower()
# vowel = 'aeiou'
# if ch in vowel:
#     print("Vowel")
# else:
#     print("Consonant")


# * QUESTION 4: Given a COMMA SEPARATED string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# colors = set(input("Enter three primary colors separated by comma: ").split(', '))  
# primary_colors = {"red", "blue", "yellow"}
# if colors == primary_colors:
#     print('All primary colors')
# else:
#     print('Not all primary colors')


# * QUESTION 5: Given a string message entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# user_message = input("Enter a word: ")
# high_priority_words = ("urgent", "important", "immediate")
# if "urgent" in user_message or "important" in user_message or "immediate" in user_message:
#     print("High priority message")
# else:
#     print("Normal message")

# * QUESTION 6: Given a string filename supplied by the user, write an if statement to check if the filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise print "Not an image file".
# filename = input("Enter file name: ")
# if filename.endswith(('.jpg', '.png', '.gif')):
#     print("Image file")
# else:
#     print("Not an image file")


# * QUESTION 7: Given a string email collected from the user, write an if statement to check if the email contains both "@" and "." characters. Print "Valid email" if it does, otherwise print "Invalid email".
# email = input("Enter email address: ")   
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# * QUESTION 8: You have a variable day provided by user input which can be any day of the week (e.g., "Monday", "Tuesday", etc.). Write an if statement that prints "Weekend" if the day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# user_input = input("Enter any day of the week: ").lower()
# if user_input == "saturday" or user_input == "sunday":
#     print("Weekend")
# else:
#     print("Weekday")


# * QUESTION 9: Write a program that takes a word from the user and then tells us if the number of characters of that word is up to 10 or not.
# user_input = input("Enter a word: ")
# if len(user_input) >= 10:
#     print("Up to 10 characters")
# else:
#     print("It is less than 10 characters")

# * QUESTION 10: Given the list data = [10, 20, 30, 10], write a program that checks if the first and last items are equal.
# data = [10, 20, 30, 10]
# if data[0] == data[-1]:
#     print("The first and last items are equal")
# else:
#     print("The first and last items are not equal")

# user = input("Enter a word: ")
# last_five_characters = user[-5:]
# if last_five_characters == last_five_characters[::-1]:
#     print("Yes")
# else:
#     print("No")