#
# Task 3:
# Implement a function that takes a string as input and returns a new string, containing only numbers.
# Each number represents the position of the character in the alphabet. Ignore non alpha symbols like spaces,
# puntuation, etc. If the char is lower than 10 append 0.
# Do the solution with O(n) complexity.
#
# >>> alphabet_position("Hello, World!")
# '0805121215, 2315181204!'

def translate(string):
    string = string.lower()
    new_str = ''
    for chr in string:
        if chr in alphabet:
            if alphabet[chr] < 9:
                new_str += '0' + str(alphabet[chr])
            else:
                new_str += str(alphabet[chr])
        else:
            new_str += chr
    return new_str
alphabet = {l: i+1 for i, l in enumerate(list(map(chr, range(ord('a'),ord('z')+1))))} #yes, i'm doing dict instead of using list, yes I'm strange))

def main():
    string = "Hello, World!"
    print(translate(string))
    print(alphabet)

if __name__ == "__main__":
    main()