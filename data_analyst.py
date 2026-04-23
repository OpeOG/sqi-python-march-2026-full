import re
with open("reviews.txt", "r") as f:
    contents = f.read()

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, contents)

phone_pattern = r"\+234 \d{3} \d{3} \d{4}"
phone_numbers = re.findall(phone_pattern, contents)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

with open("phone_numbers.txt", "w") as f:
    for phone in phone_numbers:
        f.write(phone + "\n")
print(emails)
print(phone_numbers)
