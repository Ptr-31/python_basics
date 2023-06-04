# Task 2:
# Implement a function that takes a list of integers as input and returns a new list with the integers sorted
# in descending order. For example, if the input list is [3, 7, 1, 5, 2, 9], the output list should be [9, 7, 5, 3, 2, 1].
#
# Note: You shall implement the sorting algorythm, do not use ready .srot() functions.
# Any algorythm is relvant, choose one by your preference - bubble, insertion, selection; Advanced ones:
# merge, quick, interpolation etc...
#
# >>> descending_sort([3, 7, 1, 5, 2, 9])
# [9, 7, 5, 3, 2, 1]
# >>> descending_sort([10, 5, 1, 20, 15])

def sort(array):
    for i, number in enumerate(array):
        j = i-1
        while(j >= 0 and array[j] < array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array

def main():
    array = [3, 7, 1, 5, 2, 9]
    print(sort(array))

if __name__ == '__main__':
    main()