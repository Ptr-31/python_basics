# Task 11:
# Implement a function that takes a list of tuples as input and returns a dictionary where the keys are the
# first elements of the tuples and the values are lists containing the second elements of the tuples that share
# the same first element.
# Think of what data structure (list, set, dict) you might use to make your life easier.
# Do the solution with O(n) complexity.
#
#
# >>> group_by_first([(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')])
# {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
# >>> group_by_first([(1, 'x'), (1, 'y'), (2, 'z')])
# {1: ['x', 'y'], 2: ['z']}
# >>> group_by_first([(1, 'p'), (2, 'q'), (3, 'r'), (1, 's'), (3, 't')])
# {1: ['p', 's'], 2: ['q'], 3: ['r', 't']}

def group_by_first(list_of_tuples: list):
    list_of_tuples = sorted(list_of_tuples)
    dictionary = {i[0]: [] for i in list_of_tuples}
    for i, item in enumerate(list_of_tuples):
        if item[1] not in dictionary[item[0]]:
            dictionary[item[0]].append(item[1])
    return dictionary

def main():
    list_of_tuples = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
    print(group_by_first(list_of_tuples))
    print(group_by_first([(1, 'x'), (1, 'y'), (2, 'z')]))
    print(group_by_first([(1, 'p'), (2, 'q'), (3, 'r'), (1, 's'), (3, 't')]))
if __name__ == '__main__':
    main()