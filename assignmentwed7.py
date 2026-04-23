# *************************************** QUESTION 1 ************************************************

# Scrape (the first page of) quotes from the site and perform some basic text and author-based analysis.
# Use the demo site: http://quotes.toscrape.com/
# Count total number of quotes
# Count the number of unique authors
# Find the author with the most quotes on the page
# Count how many quotes contain the word “is” (case-insensitive)
# List all tags that appear and how many times each appears

# *************************************** QUESTION 2 ************************************************
# Objective: Create a Python project that reads data from a file, processes it using a custom module, and fetches 
# additional information from the web using a third-party library. Organize your code into packages and modules to 
# structure the project effectively.

# Instructions:
# Create a Package and Module:
# Create a package named data_processing.
# Inside data_processing, create two modules:
# file_reader.py for reading and processing data from a file.
# web_fetcher.py for fetching additional information from a web API.

# ii-----> File Handling
# Create a text file named data.txt with the following content:
# Alice,30
# Fiona,28
# Jasmine,31
# George,33
# Bob,25
# Ella,22
# Hannah,27
# Daniel,40
# Isaac,29
# Charlie,35

# iii -----> 	Custom Module (do this in file_reader.py):
# Implement a function read_data(file_path) that reads the content from data.txt, parses it, and returns a list of tuples containing names and ages. e..g [("Alice", 30), ("Fiona", 28), ...]

# iv -----> 	Third-Party Library (do this in web_fetcher.py):
# Use the requests library to fetch data from the public API JSONPlaceholder
# Implement a function fetch_user_data() that retrieves and returns a list of user names from the API.

# v ------> 	Main Script:
# 	Create a main script main.py that:
# Imports functions from the file_reader and web_fetcher modules.
# Reads data from data.txt using file_reader.read_data().
# Fetches user data using web_fetcher.fetch_user_data().
# Prints the data from the file and the web.

# vi ------> 	Before you begin, make sure you:
# Create a virtual environment for your project.
# Install the requests library within this environment.
# Ensure that the virtual environment is used when running your main script.

# Expected Project Structure:
# ├── data_processing
# │   ├── file_reader.py
# │   ├── __init__.py
# │   └── web_fetcher.py
# ├── data.txt
# └── main.py

# Hints:
# For reading files, use Python’s built-in open() function.
# For web requests, use requests.get() from the requests library.
# For package organization, remember to include an empty __init__.py file in the data_processing package directory.

# *************************************** QUESTION 3 ************************************************
# Scenario:
# You are working as a data analyst for a marketing company. You have been given a large text document containing customer reviews and feedback. Your task is to extract all email addresses and phone numbers from this document for further analysis.

# Task:
# Write a Python script named `data_analyst.py` that:
# Reads the contents of a text file named reviews.txt.
# Extracts all email addresses and phone numbers from the text.
# Email addresses follow the standard format: username@domain.tld
# Phone numbers are in the format: +234 803 456 7890
# Writes the extracted email addresses to a file named emails.txt and the phone numbers to a file named phone_numbers.txt.

# Requirements:
# Use regular expressions to find the email addresses and phone numbers.
# Ensure that the extracted data is saved in separate files, one for emails and one for phone numbers.

# Example:
# Given the following content in reviews.txt:

# Customer feedback:
# - Email: john.doe@example.com
# - Phone: +234 803 456 7890
# - Another contact: jane_smith@workplace.org
# - Alternate phone: +234 701 234 5678

# The script should produce:
# emails.txt containing:
# john.doe@example.com
# jane_smith@workplace.org
# phone_numbers.txt containing:
# +234 803 456 7890
# +234 701 234 5678

# 	Go here and download the `reviews.txt` file to use.




