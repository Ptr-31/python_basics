# Implement a function that takes a list of integers as input and returns a new list with
# only the even integers from the input list. For example, if the input list is [1, 2, 3, 4, 5, 6],
# the output list should be [2, 4, 6].
# Do the solution with O(n) complexity.
#
#
# >>> even_numbers([1, 2, 3, 4, 5, 6])
# [2, 4, 6]
# >>> even_numbers([7, 8, 9, 10, 11, 12])
# [8, 10, 12]
# >>> even_numbers([0, 1, 2, 3, 4, 5])
# [0, 2, 4]
def even(array):
    new_arr = []
    for number in array:
        if number % 2 == 0:
            # print(number)
            new_arr.append(number)
    return new_arr

def main():
    arr = [1, 2, 3, 4, 5, 6]
    even_arr = even(arr)
    print(even_arr)

if __name__ == "__main__":
    main()