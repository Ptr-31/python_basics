# Task 6:
# Implement a function that takes a string as input and returns the frequency of each character in the string.
# Think of what data structure (list, set, dict) you might use to make your life easier.
# Do the solution with O(n) complexity.
# >> > char_frequency("hello")
# h->1
# e->1
# l->2
# o->1

def chat_frequency(frequency: str):
    dict_from_set = dict.fromkeys(frequency, 0)
    for letter in frequency:
        if letter in frequency:
            dict_from_set[letter] += 1
    return dict_from_set

def print_dict(dictionary: dict):
    for item in dictionary:
        print(item, "->", dictionary[item])

def main():
    print_dict(chat_frequency("hello"))

if __name__ == "__main__":
    main()