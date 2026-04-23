# Question 1; Create a variable named `car_name` and assign the value Volvo to it.
# car_name = "Volvo"

# Question 2; Create a variable named x and assign the value 50 to it.
# Answer: x = 50

# Question 3; Which of the following variable names is legal in Python?
# a) -my_var1
# b) my-var2
# c) 123variable
# Answer: b  I think this is wrong by the way or not suitable enough

# Question 4; Which of the following assignment statements is safe in Python?
# a) print = ‘paper’
# b) in = True
# c) not = False
# d) name = “John”
# Answer: d

# Question 5; Declare variables name, age, height, and is_student, and assign them values of different types. Print the type of each variable.
# Answer:
name = "Nelson"
print(type(name))
age = 25
print(type(age))
height  = "5'9"
print(type(height))
is_student = True
print(type(is_student))

# Question 6; Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
# Answer:
first_name = "John"
last_name = "Doe"
print(first_name + last_name)

# Question 7; Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
# Answer:
message = "Hello, "
print(f"{message}Alice")

# Question 8; Create a multi-line string variable using triple quotes.
# Answer:
home_address = """Looking for a tech-school to learn your dream tech course and you're confused, SQI got you covered, they are situated at
Sqi College of technology
Heritage Mall
Dugbe, Ibadan
"""
print(home_address)

# Question 9; Create a string variable word with the value "Python". Print the first and last characters using indexing.
# Answer: 
reptile = "Python"
print(reptile[0])
print(reptile[5])
print(reptile[-1])

# Question 10; Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
# Answer:
# I don't understand IMMUTABILITY
reptile = "Python"
# reptile[2] = "t"

# Question 11; Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
# Answer: 
greeting = "Hello, World!"
greeting = "Hello, Alice"
print(greeting)

# Question 12; Given the string course_name = "Introduction to Python", use slicing to print:
# The word "Introduction".
# The word "Python".
# Answer: 
course_name = "Introduction to Python"
print(course_name[0:12])
print(course_name[-6:])

# Question 13; Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# The substring "To be or not to be".
# The substring "that is the question".
# Answer:
quote = "To be or not to be, that is the question."
print(quote[0:18])
print(quote[-21:])

# Question 14; Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# slicing to print:
# The last 5 characters.
# All characters except the last 7.
# Answer:
phrase = "A journey of a thousand miles begins with a single step"
print(phrase[-5:])
print(phrase[:-7])

# Question 15; 	Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).
# Answer:
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[::2])
print(alphabet[::3])

# Question 16; 	Given the string word = "tenet", use slicing to:
# Reverse the string and print the result.
# Answer: 
word = "tenet"
print(word[::-1])

# Question 17; Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19. (Python is f)
# Every second character from index 0 to 10. (Lann y)
# Every third character from the beginning to the end. (LrnPh  nnrai!)
# Answer:
sentence = "Learning Python is fun and rewarding!"
print(sentence[9:20])
print(sentence[:11:2])
print(sentence[::3])


# Qusetion 18; Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character.
# Answer:
programming_language = "Javascript"
print(programming_language[0:1])
print(programming_language[-1:])

# Question 19; Given the string data = "DataScience", use slicing to:
# Print the substring "Science".
# Answer:
data = "DataScience"
print(data[-7:])

# Question 20; Given the string greeting = "Good Morning!", use slicing to:
# Print every second character.
# Answer: 
greeting = "Good Morning!" 
print(greeting[::2])

# Question 21; Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.
# Answer: 
name = "Alexander"
# print(name[0:3]) 
# print(name[-3:])
result = name[0:3] + name[-3:]
print(result)







