# You are given a string that contains a list of email addresses separated by commas.
# Write a Python function that uses regex to extract all the email addresses
# from the string and returns them as a list.
# Use regexr.com or similar tool to test your regex.
#
# >>> extract_emails("My email is john@example.com, but you can also reach me at jane@example.com.")
# ['john@example.com', 'jane@example.com']

import re

def extract_emails(string_with_emails: str) -> list:
    result = re.findall(r'\w+@\w+\.\w+', string_with_emails)
    return result

def main():
    result = extract_emails("My email is john@example.com, but you can also reach me at jane@example.com.")
    print(result)
if __name__ == '__main__':
    main()
