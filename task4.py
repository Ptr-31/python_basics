#
# Implement a function that takes a string as input and returns a new string where each alphabetic character is
# shifted to the right by a given amount. For example, if the input string is "abc" and the shift amount is 2,
# the output string should be "cde". If the shift amount is greater than 26, the function should wrap around to
# the beginning of the alphabet.
# Try to use modulus operand.

def shift_letters(letters: str, step: int):
    arr = [i for i in letters]
    low_case_num_arr = [i for i in range(ord('a'), ord('z')+1)]
    upper_case_num_arr = [i for i in range(ord('A'), ord('Z')+1)]
    for i, symbol in enumerate(arr):
        if (ord(symbol) in low_case_num_arr):
            arr[i] = chr(((ord(symbol)) - ord('a') + step) % 26 + ord('a'))
        elif(ord(symbol) in upper_case_num_arr):
            arr[i] = chr(((ord(symbol)) - ord('A') + step) % 26 + ord('A'))
    return "".join(arr)

def main():
    str = 'XyZ'
    print(shift_letters(str, 3))

if __name__ == "__main__":
    main()