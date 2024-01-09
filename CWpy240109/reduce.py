from functools import reduce

array = (5, 7, 8, 3)

result = reduce(lambda acc, x: acc + x, array)