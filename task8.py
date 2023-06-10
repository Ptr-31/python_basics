# Implement a function that takes a list of strings as input and returns a list of the unique words
# in the input list, in the order that they first appear.
# Think of what data structure (list, set, dict) you might use to make your life easier.
# Do the solution with O(n) complexity.
#
# >>> unique_words(['hello', 'world', 'hello', 'python'])
# ['hello', 'world', 'python']
# >>> unique_words(['cat', 'dog', 'dog', 'cat', 'bird', 'mouse'])
# ['cat', 'dog', 'bird', 'mouse']
# >>> unique_words(['apple', 'orange', 'banana'])
# ['apple', 'orange', 'banana']

def unique_words(words: list[str]):
    unique = set(words)
    return unique

def unique_words_arr(words: list[str]):
    arr = []
    for single_word in words:
        if single_word not in arr:
            arr.append(single_word)
    return arr

def main():
    print(unique_words(['hello', 'world', 'hello', 'python']))
    print(unique_words_arr(['cat', 'dog', 'dog', 'cat', 'bird', 'mouse']))

if __name__ == "__main__":
    main()

# def unique_words(list1: list[str]):
#     data = dict()
#     value = "unique"
#     array = []
#     for i in list1:
#         if i not in data:
#             data[i] = value
#     for key, value in data.items():
#         array.append(key)
#     return array
#
#
# def main():
#     mylist = ['hello', 'world', 'hello', 'python']
#     print(unique_words(mylist))
#
#
# if __name__ == "__main__":
#     main()