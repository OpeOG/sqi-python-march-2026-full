# Question 1; Assign values "Orange", "Banana", "Cherry" to multiple variables x,y and z in one line respectively.
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# Question 2; Assign the values 10, "John", and True to the variables age, name, and is_student in a single line.
age, name, is_student = 10, "John", True
print(age, name, is_student)

# Question 3; Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
x = 5
y = 10
x, y = y, x
print(x, y)

# Question 4; Create a list of numbers with values 1,2 and 3. Unpack the list into seperate variables a,b and c.
Numbers = [1, 2, 3]

a, b, c = Numbers
print(a)
print(b)
print(c)

# Question 5; Convert a string "James John Kennedy" called "names" to a list using the string .split() method. Store the result in a list called "names_list"
names = "James John Kennedy"
names_list = names.split()
print(names.split())

# Question 6; You have a list of cities called cities_list containing ['New York', 'Los Angeles', 'Chicago']. Convert this list into a single string where each city is seperated by a semicolon and a space. Store the result in a string called cities_string.
cities_list = ['New York', 'Los Angeles', 'Chicago']
cities_string = '; '.join(cities_list)
print(cities_string)

# Question 7; Create a string variable sentence with the value "the quick brown fox jumps over the lazy dog". Capitalize the first letter of the string and print the result.
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

# Question 8; Create a string variable book_title with the value "to kill a mockingbird". Capitalize the  first letter of each word and print the result.
book_title = "to kill a mockingbird"
print(book_title.title())

# Question 9; Create a string variable text with the value "hello world". Count the number of occurrences of the letter 'o' and print the result.
text = "hello world"
print(text.count('o'))

# Question 10; Create a string variable filename with the value "document.txt". Check if the string starts with "doc" and print the result.
filename = "document.txt"
print(filename.startswith('doc'))

# Question 11; Create a string variable url with the value "https://www.example.com". Check if the string ends with the ".com" and print the result.
url = "https://www.example.com"
print(url.endswith('.com'))

# Question 12; Create a string variable phrase with the value "find the needle in the haystack". Find the position of the word "needle" and print the result.
phrase = "find the needle in the haystack"
print(phrase.find('needle'))

# Question 13; Create a string variable template with the value. "Hello,{}. Welcome to {}.". Use the format{} method to replace the placeholders with "Alice" and "Wonderland" and print the Result. Bonus point if you can do it with the with the f-string and concatenation methods also.
name = "Alice"
place = "Wonderland"
print("Hello, {} Welcome to {}.". format(name, place))
print(f"Hello, {name} Welcome to {place}.")
result = "Hello, " + name + "Welcome " + "to " + place
print(result)

# Question 14; Create a string variable quote with the value "To be or not to be". Find the position of the word "not" and print the result.
quote = "To be or not to be"
print(quote.find('not'))

# Question 15; Create a string varaible word with the value "hello". Check if all characters in the string are lowercase and print the result.
word = "hello"
print(word.islower())

# Question 16; Create a string variable shout with the value "HELLO". Check if all characters in the string are uppercase and print the result.
shout = "HELLO"
print(shout.isupper())

# Question 17; Create a string variable mixed_case with the value "PyThOn". Convert all characters to uppercase and print the result.
mixed_case = "PyThOn"
print(mixed_case.upper())

# Question 18; Create a string variable padded_text with the value " hello". Remove leading whitespace and print the result.
padded_text = " hello "
print(padded_text.lstrip())

# Question 19; Create the string variable padded_text with the value " hello ". Remove trailing whitespace and print the result.
padded_text = " hello "
print(padded_text.rstrip())

# Question 20; Create the string variable padded_text with the value " hello ". Remove both the leading and trailing whitespace and print the result.
padded_text = " hello "
print(padded_text.strip())

# Question 21; Create a string variable greeting with the value "Hello,World!". Replace "World" with "Alice"  and print the result.
greeting = "Hello,World!"
print(greeting.replace('World','Alice'))