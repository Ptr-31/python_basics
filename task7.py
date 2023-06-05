# Task 7:
# Implement a function that takes two lists of integers as input and returns a list containing the
# common elements between the two input lists, in ascending order.
# Think of what data structure (list, set, dict) you might use to make your life easier.
# Do the solution with O(n) complexity.
#
#
# >>> common_elements([1, 2, 3, 4], [3, 4, 5, 6])
# [3, 4]
# >>> common_elements([5, 2, 8, 9], [1, 2, 8, 9])
# [2, 8, 9]
# >>> common_elements([1, 3, 5], [2, 4, 6])
# []

def common_elements(list_one: list, list_two: list)->list:
    set_one = set(list_one)
    set_two = set(list_two)
    set_two &= set_one
    return list(set_two)

def main():
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(common_elements([5, 2, 8, 9], [1, 2, 8, 9]))

if __name__ == "__main__":
    main()