#Regex means regular expression
# It is a special pattern used to search, match, extract, or replace text.
# Think of regex like a smart text detector.
# Instead of checking text letter by letter manually, you write a pattern and tell Python:
# find text that looks like this
# extract text that follows this rule
# replace text that matches this shape

# So regex is not ordinary text. It is a rule for describing text.

# r"\d+" ----> means one or more digits, that can match 1, 25, 123456
# \d = any digit from 0 to 9
# + = one or more of the thing before it.
# r means raw string, it tells python treat backlashes normally, do not interpret them as special Python escape characters first.
# import re

# # Example 1: Simple match
# pattern = r"\bword\b"
# text = "A word in a sentence."
# match = re.search(pattern, text)
# if match:
#     print(match)
#     print("Match found:", match.group())  # Match found: word
# hint; word = the actual word you want, the \b = word boundary(which means, the word must stand alone, not be part of another word.)
# note: assume text = "word sword wording"
# pattern = r"word"
# could match "word" inside "sword" too. but r"\bword\b" matches only the standalone "word", that's why the \b is useful.

# matching

# # Example 2: Find all occurrences
# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']
# hint; search() = first match only
# findall() = all matches

# Example 3: Replace text
# pattern = r"\s+"
# text = "This   is a test."
# new_text = re.sub(pattern, " ", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.
# hint; \s = whitespace
# + = one or more
# so \s+ means one or more whitespace characters
# re.sub() means substitute, or replace
# so this question is basically requesting for you to replace all groups of spaces with a single space.


# # Example 4: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "Contact us at support@example.com for more info."
# match = re.search(pattern, text)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com
# hint; [a-zA-Z0-9._%+-]+ means:
# match one or more of these:
# lowercase letters a-z
# uppercase letters A-Z
# numbers 0-9
# dot .
# underscore _
# percent %
# plus +
# minus -
# this is the part before @ so it matches something like this; support, john.doe, user123

# [a-zA-Z0-9.-]+
# matches the domain name part like;
# example
# gmail
# my-site
# \. means a literal dot. why blackslash? because dot(.) in regex normally means any character so \. means actual full stop

# # Example 5: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']
# hint; \d{4} = exactly 4 digits
# - = dash
# \d{2} = exactly 2 digits
# - = dash
# \d{2} = exactly 2 digits. So it matches 2023-08-15
# {4} means repeat exactly 4 times, {2}  means repeat exactly 2 times
# \b at both ends helps ensure it behaves like a complete date pattern

# Example 6: Validate phone number
# pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
# phone_number = "(123) 456-7890"
# if re.match(pattern, phone_number):
#     print("Valid phone number")  # Valid phone number
# else:
#     print("Invalid phone number")

# Break it down:
# ^ = start of string
# \( = literal opening bracket
# \d{3} = 3 digits
# \) = literal closing bracket
# space
# \d{3} = 3 digits
# - = dash
# \d{4} = 4 digits
# $ = end of string
# So it must look exactly like (123) 456-7890

# ^ and $ matter means start here and end here
