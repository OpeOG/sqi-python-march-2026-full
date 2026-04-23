# QUESTION 1: Create a function called multiply_first_two that returns the product of the first two numbers passed in.
# def multiply_first_two(*numbers: int):
#     return numbers[0] * numbers[1]
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# QUESTION 2: Create a function called describe_books that prints out each book title and its author.
# def describe_books(**books: dict):
#     for title, author in books.items():
#         print(f"{title} is written by {author}")
# describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")
# describe_books(Matilda="Roald Dahl", Book1984="George Orwell")

# QUESTION 3: Create a function called total_age that returns the sum of all the ages given.
# def total_age(*ages):
#     sum_of_ages = 0
#     for age in ages:
#         sum_of_ages += age
#     return sum_of_ages
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# QUESTION 4: Create a function called list_countries that prints out each country passed in.
# def list_countries(*countries):
#     for country in countries:
#         print(country)
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# QUESTION 5: Create a function called student_details that prints each student’s name and score.
# def student_details(**students):
#     for student, score in students.items():
#         print(f"{student} scored {score}")
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# QUESTION 6: Create a function called average_score that returns the average of all scores passed in.
# def average_score(*scores):
#     total = 0
#     for score in scores:
#         total += score
#     return total / len(scores)
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# QUESTION 7: Create a function called total_price that adds up the prices of all items passed as keyword arguments.
# def total_price(**items):
#     total = 0
#     for item, price in items.items():
#         total += price
#     return total
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# QUESTION 8: Create a function called first_and_last that prints the first and last values passed in.
# def first_and_last(*values):
#     first = values[0]
#     last = values[-1] 
#     print(f"First: {first}")
#     print(f"Last: {last}")
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# QUESTION 9: Create a function called describe_animals that prints out animal and their sound.
# def describe_animals(**animals):
#     for animal, sound in animals.items():
#         print(f"{animal} makes the sound {sound}")
# describe_animals(cat="meow", dog="bark", cow="moo", snake="hiss", lion="roar")

# QUESTION 10: Create a function called total_characters that returns how many characters in total exist in all keyword values.
# def total_characters(**words):
#     total = 0
#     for value in words.values():
#         total += len(value)
#     return total
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))
    
# QUESTION 11: Create a function called find_minimum that returns the smallest number from all the values passed in.
# def find_minimum(*values):
#     smallest_num = values[0]
#     for value in values:
#         if value < smallest_num:
#             smallest_num = value
#     return smallest_num
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))        

# QUESTION 12: Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.
# def sum_scores_and_bonuses(*scores, **bonuses):
#     total = 0
#     for score in scores:
#         total += score
#     for bonus in bonuses.values():
#         total += bonus
#     return total
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

#*************OR****************
# def sum_scores_and_bonuses(*scores, **bonuses):
#     return sum(scores) + sum(bonuses.values())


# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))


# QUESTION 13: Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).
# def longest_word(*args, **kwargs):
#     longest = ""
#     for word in args:
#         if len(word) > len(longest):
#             longest = word
#     for word in kwargs.values():
#         if len(word) > len(longest):
#             longest = word
#     return longest
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

#***********OR****************
# def longest_word(*args, **kwargs):
#     return max(list(args) + list(kwargs.values()), key=len)


# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))