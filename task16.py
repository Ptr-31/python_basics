# Write a Python program that takes in a list of email addresses as input and returns a dictionary with the number of
# email addresses from each domain. Your program should use regular expressions to extract the domain name from each email
# address.
#
# The input to the program should be a list of email addresses in the following format:
# [
#     "user1@example.com",
#     "user2@subdomain.example.com",
#     "user3@example.net",
#     "user4@example.com"
# ]
# The output of the program should be a dictionary with the number of email addresses from each domain, like this:
# {
#     "example.com": 2,
#     "subdomain.example.com": 1,
#     "example.net": 1
# }
# To complete this task, you will need to use regular expressions to extract the domain name from each email
# address in the input list. You can use the re module in Python to work with regular expressions.

import re
def search(inp: list) -> dict:
    domains_dict = {}
    for line in inp:
        search = re.search(r'@\w+.\w+.\w+', line)
        search = search.group()
        if domains_dict.get(search) is None:
            domains_dict[search] = 1
        else:
            domains_dict[search] += 1
    return domains_dict
def main():
    inp = [
        "user1@example.com",
        "user2@subdomain.example.com",
        "user3@example.net",
        "user4@example.com"
    ]
    print(search(inp))
    # print(inp)
if __name__ == '__main__':
    main()
