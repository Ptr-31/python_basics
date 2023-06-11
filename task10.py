# Task 10:
# Implement a function that takes a list of numbers and returns a tuple containing the minimum and maximum values in the list.
# IMPORTANT NOTE, for implement:
# - Use built-in python functions to find the minimum and maximum values.
# - Use the ability to assign values to multiple variables on a single line.
#
# >>> min_max_values([1, 3, 6, 5, 3, 2, 1, 5, -1, 5, 2, 10, 4, 3])
# (-1, 10)

def min_max_values(list_of_values: list[int]) -> tuple((min, max)):
    return ((min(list_of_values), max(list_of_values)))

def main():
    print(min_max_values([1, 3, 6, 5, 3, 2, 1, 5, -1, 5, 2, 10, 4, 3]))
if __name__ == '__main__':
    main()