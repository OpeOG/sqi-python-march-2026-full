# A dictionary is a collection type that stores its item in key: value pair
# We don't have indexing in a dictionary
# It always one key to one value . Item is made up of a key and an item
# A dictionary is ordered
# person = ["Dada Oluwatobi", "Computer Science", "University of Ibadan", "Python Dev", 2009]

# person = {
#      'name' : "Dada Oluwatobi",
#     'dept' : "Computer Science",
#     'school' : "University of Ibadan",
#     'skill' : "Python Dev",
#     'graduation_year' : 2009
# }
# print(person)

# ['Cheetah', 'Lion', 'Tiger']
# {'animal1': "Cheetah", 'animal2': "Lion", 'animal3': "Tiger"}


# Accesing items in a dictionary
# print(person['name'])
# print(person['skill'])
# print(person['graduation_year'])

# Python throws error if the key doesn't exist in the dictionary
# e.g 
# print(person['age'])

# Accessing values of items in a dictionary using the exact type used when orignally creating the dictionary
# numbers = {
#     '1': "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     2: "Twenty-two"
# }
# print(numbers[2])  # this will give us "Twenty-two"
# print(numbers['2']) # Gives us Two

# Creating an empty dictionary
# animals = {}

# #Adding items into a dictionary
# animals['lion'] = "Roars"
# animals['goat'] = "bleet"
# print(animals)

# animals['bird'] = "Chirps"
# animals['bird'] = "Roars" # Keys already exists, therefore, value is updated to "Roars"
# animals['snake'] = "Hisses"
# animals['dog'] = "Barks"
# print(animals)

# # Deleting a item from a dictionary
# del animals['dog']
# print(animals)
# del animals['eagle'] # this will give us an keyerror because it does not exist in the dictionary

# translations = {
#     'go': "lo",
#     'question': "ibeere",
#     'eat': "jeun",
#     'unclad': "bo aso",
#     'i am going': "mo ti n lo"
# }

# word_to_translate = input('Enter word in english: ').lower()

# translated_word = translations[word_to_translate]

# print(f"\"{word_to_translate}\" translated to yoruba is : \"{translated_word}\"")

# Ordered, Does not allow duplicate keys
# person = {'fname': "Oluwatobi", 'lname': "Dada", 'fname': "John", 'mname': "Ephraim"}

# Write a program that first creates an empty dictionary called employee_persona. Then, accept emp_id, emp_name, emp_date, employment year from the user and then store them in the dictionary. 

# employee_persona = {}
# emp_id = input('Enter your emp_id: ')
# emp_name = input('Enter your emp_name: ')
# emp_date = input('Enter your emp_date: ')
# emp_year = input('Enter your emp_year: ')

# employee_persona['empid'] = emp_id
# employee_persona['empname'] = emp_name
# employee_persona['empdate'] = emp_date
# employee_persona['empyear'] = emp_year
# print(employee_persona)

# Finding out whether a key exists in our dictionary
# users = {
#     'tobi' : "Dada Oluwatobi John",
#     'lekan': "Olalekan Ajanlekoko",
#     'rose': "Rosetta Roseline"
# }
# print("tobi" in users)
# print("Olalekan Ajanlekoko" in users) # this will be False because it's not the key

# Replace the password of a user
# from getpass import getpass
# user = {'username': 'oluwato1000', 'password': "Oluw%$$"}
# print(f"Hi, {user['username']}, your password has been breached.")

# password = getpass(" Provide new password below: \n")

# user['password'] = password
# print("Password updated successfully")
# print(user)

# thisisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisisdict)

# users = {
#     'tobi' : "Dada Oluwatobi John",
#     'lekan': "Olalekan Ajanlekoko",
#     'rose': "Rosetta Roseline"
# }

# print(f"There are {len(users)} users in my table")

# *************************DICTIONARY METHODS**************************
# get method
# translations = {
#        'go': "lo",
#     'question': "ibeere",
#     'eat': "jeun",
#     'unclad': "bo aso",
#     'i am going': "mo ti n lo"
# }
# print(translations.get('go'))
# print(translations.get('come',)) # You will get "none" by default
# print(translations.get('come', 'Undefined')) # this will give us "undefined"

# # Using the update() method on a dictionary
# # read => kawe
# # code => sashe

# translations['read'] = 'kawe' # normal way
  
# # or use the update method
# translations.update({'read': 'kawe', 'code': 'sashe'})

# # OR

# translations.update(bite = "ge je")
# print(translations)

# # Removing an item from a dictionary
# removed_translations = translations.pop('question')
# print(translations)

# print(removed_translations)
# translations.update({'question': removed_translations})

# # Removing the last item from the dictionary
# print(translations)
# translations.popitem()
# print(translations)
# # OR
# popped = translations.popitem()
# print(popped)

# # Clearing your dictionary
# translations.clear()

# data = {
#     'user1': {
#       'name': "Tobi",
#     'location': "Ibadan",
#     'workplace': "Nigeria"
#     }, 
#     'user2': "John",
#     'location': "Ado-Ekiti",
#     'workplace': "Nigeria"

# }
# print(data['user1']['workplace'])

# admin_copy = data.copy()

# admin_copy.popitem()
# print('ADMIN: ', admin_copy)
# print('Normal copy; ', data)

# translations = {
#        'go': "lo",
#     'question': "ibeere",
#     'eat': "jeun",
#     'unclad': "bo aso",
#     'i am going': "mo ti n lo"
# }
# keys = translations.keys() #gives us back a readonly version of all keys in your dictionary
# translations.popitem()
# print(keys)


# print(translations.keys()) # this will print out only the keys. 
# print(list(translations.keys()) )  # this will give us the list
# print(list(translations.values()) )  # this will give us the list and values


# Finding out whether a particular value exists in a dictionary [whether among the keys or values]
# print('eat' in translations.keys() or 'eat'  in translations.values)

# The items() method gives us back a readonly version of our keys and vakues in form of a list of tuples
# print(translations.items()) # this will add the key and value in a tuple
# translations_tuple = list(translations.items()) # this will be created seperately
# print(translations_tuple)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(len(car))
car.update(year = 2022)

x = car.items() # The items() method will return each item in a dictionary, as tuples in a list.
print(x)

x = car.keys() # This will print out all the keys
print(x)

x = car.values()   # This will print out all the values 
print(x)


# Let's update the value of the key "brand" to "Toyota"
car["brand"] = "Toyota"
print(x)

# Let's add a new key "driver" to our dictionary, so will check if the key exist already, if doesn't it will create a new key and add it to the dictionary. 
car['driver'] = "Salisu"
print(x)
