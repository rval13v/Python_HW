from itertools import zip_longest
numbers_1 = [1, 2, 3, 4, 7, 4]
numbers_2 = [1, 2, 3, 3, 3]
sums = [x + y for x, y in zip_longest(numbers_1, numbers_2, fillvalue=0)]
print(sums)