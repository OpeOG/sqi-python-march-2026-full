# with open("for_loops.py", "r") as f:
#     # contents = f.read()
#     lines = f.readlines()


# print(contents)
# print(lines)

# for idx, line in enumerate(lines, start=1):
#     print(f"Line {idx}", line)

# with open("new_file.txt", "w") as f:
#     f.write("This line was written using Python")


# with open("new_file.txt", "a") as f:
#     f.write("This is another line that was written using Python\n")


# f = open("new_file.txt", "r")
# print(f.read())
# f.close()

# module - python file, usually part of a larger package.
# script - python file that has a single responsibility and is not needed after that responsibility is fulfilled. It is not usually part of a larger program/package.
# package - a folder containing python modules usually with an __init__.py file.

# *************** ANOTHER WORK******************
# with open("cbt.py", "r") as f:
#     contents = f.read()
#     lines = f.readlines()
# print(contents)
# print(lines)

# for idx, line in enumerate(lines, start=1):
#     print(f"Line {idx}", line)

# with open("cbt.py", "w") as f:
#     f.write("This line was written using Python")

# with open("cbt.py", "a") as f:
#     f.write("This new line will be added to the file i opened")

# *********************PSL ***************************
# from datetime import datetime

# now = datetime.now()

# import datetime

# now = datetime.datetime.now()

# print(now)


# sixteenth_mar_2025 = datetime.date(2025, 3, 16)
# print(sixteenth_mar_2025)

# one_week = datetime.timedelta(weeks=1)

# one_week_after_sixteenth = sixteenth_mar_2025 + one_week
# print(one_week_after_sixteenth)

# 23/03/2025

# strptime -> string parse time (str -> date)
# strftime -> string format time (date -> str)

# one_week_after_sixteenth_str = one_week_after_sixteenth.strftime("%Y-%m-%d")
# print(one_week_after_sixteenth_str)

# now_formatted = now.strftime("%Y/%m/%d %H:%M:%S")
# print(now_formatted)

# date_str = "23 February, 2024"
# date = datetime.datetime.strptime(date_str, "%d %B, %Y")
# print(date)
# print(date + datetime.timedelta(3))


# 23 February
# February 23
# Feb 23
# 23/02
# 23-02

# *************** WRITE A CODE TO WISH SOMEONE HAPPY BIRTHDAY ************************
# import datetime

# today = datetime.datetime.now()

# user_birthday = input("Enter your birthday (Month Day): ")
# user_birthday += f", {today.year}"

# birthday = datetime.datetime.strptime(user_birthday, "%B %d, %Y")

# if birthday.date() == today.date():
#     print("Happy birthday!!!")
# elif birthday.date() < today.date():
#     print("Happy belated birthday")
# else:
#     print("Happy birthday in advance")
# *************** WRITE A CODE TO WISH SOMEONE HAPPY BIRTHDAY ************************
# a library is code you can import and use e.g "import math", "import random", "import datetime", "import os"
# a module is usually one file
# a package is a group of modules
# Examples of 3rd-party libraries eg Pandas, numpy, requests, flask
# pip - Python package installer

# PSL - Python Standard Library

import math

print(math.pi)

print(math.log10(1000))

# THIRD PARTY LIBRARIES

# PyPI - Python Packaga Index

# Creating project folder and creating virtual environment, then activate it
# 1. Create a directory for the project
# 2. Enter into the directory
# 3. Create a virtual environment with `python -m venv .venv`
# 4. Activate the virtual environment with `source .venv/bin/activate` (mac/linux) or `.venv\Scripts\activate` (windows)
# 5. Install the 3rd party libraries


# How to install "requests" and "bs4" from the beginning. Make sure your .venv(virtual environment) is active before installing this two

# requests: fetches the webpage

# BeautifulSoup: helps you read and structure the webpage content

# Step1: Type "pip install requests" in your powershell. This downloads and installs the requests library into your virtual environment.

# Step2: Your code uses this line "bs4 import BeautifulSoup", this means we need bs4, so you install it with "pip install beautifulsoup4"

# Step3: You can confirm the installed packages with "pip list" in your powershell. You should see packaages like "requests" and "beautifulsoup4"

# Easy way to put it:
# I created the web_scraping folder in the terminal using mkdir, then entered it with cd, created a virtual environment with python -m venv .venv, activated it, installed requests and beautifulsoup4, then created and ran scraping.py.

# parse = understand and organize the HTML
# prettify / beautify = display the HTML neatly

# HTTP STATUS CODE
# 200 ----> OK (the request was successful)
# 404 ----> Not Found (wrong URL, deleted page, misspelled link)
# 500 ----> Internal Server Error(this means something went wrong on the website's server. This is usually not your fault. It means the website itself has a problem.)
# 403 ----> Forbidden(server understood your request, but refuses to allow access, this happens when a page is protected, the website blocks bot, the server does not want your script accessing it.)
# 401 ----> Unathorized(this means you need permission or login before accessing the page.)
# 301/302 ----> Ridirect(the page has moved somewhere else)

# Easy way to group status codes
# 1xx = information

# The request is being processed

# 2xx = success

# Everything worked

# Example:

# 200 OK
# 3xx = redirection

# You are being sent somewhere else

# Example:

# 301 Moved Permanently
# 302 Found
# 4xx = client error

# Something is wrong with the request from the user side

# Examples:

# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 5xx = server error

# Something is wrong on the website/server side

# Examples:

# 500 Internal Server Error
# 502 Bad Gateway
# 503 Service Unavailable

# encoding="utf-8" tells Python to save the text file using UTF-8 character format so the webpage text is written correctly.