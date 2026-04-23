# Escape Characters: Python Don't see it as it is but something, take it as something special. You start with blacksplash followed by the characters. Read on the types of characters so you know them all

# e.g \n, \, \r,\b,\',\"
# /t means tab


# \n means space : The newline character (\n) is used in strings to represent the end of a line, allowing text to be split across multiple lines.When included in a string, it moves the cursor to the beginning of the next line. For example:
# print("Hello, sir, do you \n\n\n\nsee this?")



# \t    TAB. This function is for creating tabs
# print("FirstName\t\tLastName\t\tEmail") 
# print('-------------------------------------------------------------')

# \r ------- RETURN CARRIAGE TO THE BEGINNING OF THE LINE. Please ask for more explanation on this from your instructor
# print("Hi, this line works. But\rit now no longer works")


# print("This is programming/bAnd"). Get the full note on this and read on it
# \',\"\

# The man said this legendary quote "John Wick, the man, the myth, the 'Legend'"

# print('e')

# (And...... /"we're out")



# ****************INDEXING : It used for printing selected characters from a string*********************
# language = "Kotlin" 
# name = "Nelson"
# activity = "cheerleeding"
# your_string{then put the index}
# print(language[0])
# print(name[2])
# print(activity[5])

# negavtive indexing
# print(language[-2])
# print(name[-3])
# print(activity[-6])

# Have the variable fav_game ="Devil May Cry". Then have the output DDevil May Cryy
# fav_game = "Devil May Cry"
# print(fav_game[0] + fav_game + fav_game[-1])

#  or you can either do it this way

# print(fav_game[0] + fav_game + fav_game[-1])
# fav_game = "Devil May Cry"
# first_char  = fav_game[0]
# last_char = fav_game[-1]
# print(first_char + fav_game + last_char)

# a = "This is a longer string"
# print(a[1], a[2], a[10])

# month = "january"
# print jaajanuaryyy
# arjun

# print(month[0] + month[1] + month[1] + month + month[-1] + month[-1])
# print(month[1] + month[5] +month[0] + month[3] + month[2])

# day = "wednesday"
# print wedwednesdaywys
# print(day[0] + day[1] + day[2] + day + day[0] + day[-1] + day[-4])

# Note; You can't index integers or float. You get an error
# e.g ; num = 344546
# print(num[2]) ------> It will give you an Error

# *****************IMMUTABILITY************************
# Note: Python strings are immutable; that is, you cannot modify a string without creating a new string variable, or assigning a completely new string value to the variable.
#  Note: Please ask for more explanation on this from your instructor
# Immutable --------Unmodifiable
# name = "Johnson"
# name[-3] = "R"


# *************SLICING*******************
# String slicing in Python allows you to extract a part of a string using a specific syntax. The syntax for 
# slicing is: string[start_index: end_index: step]
# Note : Omitting start means starting from the beginning.
# Omitting end means slicing until the end of the string.
# Get O or more characters instead of index that gets just one character
# item = "Refrigerator"
# Slicing syntax: string[start_index: end_index: step]
# print(item[0:6])
# print(item[0:3])
# print(item[3:9])
# print(item[:5])
# print(item[5:])

# this gets us the whole string
# print(item[:])

# Slicing with the step included
# string[start:stop:step]
# print(item[0:10:2])

# print(item[::3])
# print(item[0:-6])
# print(item[:-1])
# print(item[:-3])
# print(item[-4:])

# NEGATIVE 
# item = "Refrigerator"
# print(item[::-1])     ---------> I'm not sure i understand this. Ask your instructor 
# print(item[::-2])

# Note : To reverse a string; you make use of print(text[::-1])
# Refrigeratorrotaregirfer
# print(item + item[::-1])

# item = "Concatenate"
# print(item[5])

# universe = "Milkyway"
# print(universe[-3])

# name = "Alexander"
# print(name[:3]  + name[-3:])v


