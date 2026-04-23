# # STRING METHODS 


# animal = "Jaguar"
# # jaguar
# place = "Akure"
# print(place.lower())
# print(animal.lower())

# # JAGUAR
# place = "akure"
# print(place.upper())
# print(animal.upper())
# # or
# lower_animal = animal.lower()
# print(lower_animal)


# # Capitalizing a string  [turns the first letter of a string to uppercase and every other to lower case]

# print(animal.capitalize())

# animal = "cheetah"
# print(animal)
# print(animal.capitalize())
# place = "akure"
# print(place.capitalize())



# Using the title() method of a string. This capitalize every first letter of a word.
# animal = "CHEETAH IS FAST"
# print(animal.title())
# quote = "WORTHY IS THE LAMB, HALLELUJAH"
# print(quote.title())

# animal_phrase = "the monkey's best food is Banana"
# print(animal_phrase.title())


# Using the count() method of the string ----> tells us the number of times a particular character can be found in a string
# Note; anytime you do string.count it will give you an integer
# animal = "CHEETAH IS FAST. But the fastest of all is the Perigrine Falcon"
# print(animal.count("H"))
# print(animal.count("Z"))
# print(animal.count("E"))

# counting all letter "e" in our string, regardless of their case
# lower_animal = (animal.lower())
# print(lower_animal.count("e"))
# number_of_Es = lower_animal.count('e')
# print(f"Number of 'E' in {animal} is {number_of_Es}")
# Print number of "E" in CHEETAH IS FAST. But the fastest of all is the Perigrine Falcon
# print(f"Number of 'E' in {animal} is {number_of_Es}")


# Know whether a string starts or ends with a particular character
# animal = "CHEETAH IS FAST. But the fastest of all is the Perigrine Falcon"
# print(animal.startswith("C"))
# print(animal.endswith('fly'))

# Print whether .animal starts with 'c' regardless of the case
# print(animal.lower().startswith('c'))

# to write a tuple. this means check whether it starts with a,c,b
# ('a', 'c', 'b')
# print(animal.startswith(('a', 'c', 'b')))


# Find the TOTAL LENGTH of a string
# phrase = "to be or not to be, that is the question."
# phrase_length = len(phrase)
# print(f'Length of phrase is: {phrase_length}')


# Find an index methods of the strings
# phrase = "to be or not to be, that is the question."
# print(phrase.index('E'))
# print(phrase.find('q'))
# print(phrase.find('.'))
# quote = "Worthy is the lamb, Hallelujah!"
# print(quote.index('n'))
# the only difference btw index and find is how they handle their errors. Index will write substring not found while find will write. When the (index is not found (.find) will bring -1), (index is not found (.index) will bring substring not found)
# What does even mean? --------->>>>>>Question for your tutor
# print(quote.index('b', 5))

# Checking whether a string is uppercase or lower case or is space or others
# quote = "Worthy is the lamb, Hallelujah!"
# upper_quote = (quote.upper())
# print(upper_quote.isupper())
# print(quote.islower())

# Turning everything to uppercase first and then checking whether everything has truly turned to uppercase
# print(phrase.upper().isupper())


# Stripping a string-----> Removing the spaces or new lines at the beginning or end of a string
# lstrip()
# rstrip()
#strip()
# "   Hello to the world       "
# sentence = "The quick brown for jumps over the lazy dog"
# quote = "                 Worthy is the lamb, Hallelujah!"
# print(quote.strip())
# print(len(quote))
# print(len(quote.strip()))


# # Replacing specific characters in a string
# tinubu_phrase = "Recruit...50 million youth. E lo fokan bale"
# print(tinubu_phrase.replace('million', 'billion'))
# print(tinubu_phrase.replace('fokan', '*****'))
# quote = "You're such a foolish guy and i regret helping you, you dumb fuck"
# print(quote.replace("foolish", "f******", 5))

# curse_phrase = "Get the fuck out of here, you fucked up fuck."
# print(curse_phrase.replace('fuck', '****'))

# print(curse_phrase.replace(' ', ''))

# print(curse_phrase)

# splitting a string into different items. Learn how to use comma
# phrase = "To be or not to be, that is the question."
# Note: wherever you see this (), it will split the whole string at every word since no command was given in the parenthesis
# print(phrase.split())
# print(phrase.split()[-1])
# print(phrase.split()[-2])
# print(phrase.split()[5])

# join () method takes a LIST OF STRING and turns everything to a single string
# countries = ("Guatemala", "Nigeria", "France", "Germany")
# string_separator.join(the_list)
# print('||'.join(countries))
# print('****'.join(countries))
# states = "Lagos", "Ondo", "Oyo", "Delta"
# print('*****'.join(states))



# format; Formatting a string

# book = "Harry Porter"
# author = "J.K Rowlings"
# print(f"The book {book} is written by {author}")



# # Now using the format()
# print("The book {} is written by {}". format(book, author))
# print("The book {} is written by {}". format(book, book))

# print("{} + {} = {}".format(4, 5, 4+5))

# Formatting a number into decimal places or approximation using format()
# book = "Harry Porter"
# author = "J.K Rowlings"
# price = 35.978777
# print("The {} is written by {} and it costs ${}".format(book, author, price))
# print("The {} is written by {} and it costs ${:.3f}".format(book, author,price))

# # or
# print(f"The book{book} is written by {author} and it costs ${price:.2f}")


# Seperating an email into the two parts
# email = "nelsonogunboye@gmail.com"
# email_data = email.split('@')
# print(email_data)
# username = email_data[0]
# print(username)
# domain = email_data[-1]
# print(domain)
# print(f"Your user name is: {username} and your domain is {domain}")

# username, email = email.split('@')
# print(f"Your user name is: {username} and your domain is {domain}")

# Swapping values of variables
# name, age ="John", 30
# name, age =age, name
# print(name)
# print(age)

# Swapping years
# current_year = 2026
# last_year = 2025
# next_year = 2027
# current_year, last_year, next_year = current_year, last_year, next_year
# print(current_year, last_year, next_year)
# current_year, last_year, next_year = next_year, current_year, last_year
# print(current_year, last_year, next_year)



