# Task 5:
# Implement a function that takes a string as input and returns a new string where each character is shifted to the
# right by a given amount. For example, if the input string is "abc" and the shift amount is 2, the output string
# should be "cde". If the shift amount is greater than the length of the input string, the function should wrap
# around to the beginning of the string.
# Try to use modulus operand.
# Do the solution with O(n) complexity.
#
#
# >>> shift_characters("hello", 2)
# 'llohe'
# >>> shift_characters("python", 5)
# 'npytho'

def shift_characters(letters: str, step: int):
    letters_arr = [i for i in letters]
    letters_arr = letters_arr[step % len(letters):] + letters_arr[:step % len(letters)]
    return "".join(letters_arr)

def main():
    str = 'python'
    print(shift_characters(str, 5))
if __name__ == "__main__":
    main()