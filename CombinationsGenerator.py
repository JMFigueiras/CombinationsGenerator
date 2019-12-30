import itertools
from itertools import combinations

#nCombinations = 46!/(6!*40!) = 9366819
#nAppears 1221759 => (6*9366819/46)

numbers = [0, 1, 2, 3, 4,
           5, 6, 7, 8, 9,
           10, 11, 12, 13,
           14, 15, 16, 17,
           18, 19, 20, 21,
           22, 23, 24, 25,
           26, 27, 28, 29,
           30, 31, 32, 33,
           34, 35, 36, 37,
           38, 39, 40, 41,
           42, 43, 44, 45]


for subset in itertools.combinations(numbers, 6):
    combination = str(subset).replace(")", "").replace("(","").replace(" ", "")
    print(combination)

    with open("combGenerated.txt", "a") as file:
        file.write(combination + '\n')
