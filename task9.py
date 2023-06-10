# Task 9:
# Implement a function that takes a list of tuples, where each tuple contains the name and age of a person.
# Write a Python function that takes in this list as input and returns a new list of tuples, where each
# tuple contains the name and age of the person, but with the age incremented by 1.
# Do the solution with O(n) complexity.

# >>> increment_age([("John", 25), ("Mary", 30), ("Bob", 40)])
# [("John", 26), ("Mary", 31), ("Bob", 41)]

def increment_age(array: list[tuple]):
    modified_arr = []
    for item in array:
        name, age = item
        modified_arr.append((name, age + 1))
    return modified_arr

def main():
    arr = [("John", 25), ("Mary", 30), ("Bob", 40)]
    print(increment_age(arr))

if __name__ == '__main__':
    main()
