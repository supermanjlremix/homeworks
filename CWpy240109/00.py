from functools import reduce

numbers = [2,3,4,5,6,-1]

inverted = list(map(lambda x: x * -1, numbers))
print(inverted)

evens = list(filter(lambda x: x % 2 == 0, inverted))
print(evens)

result = reduce(lambda acc, x: acc * x, evens)
print(result)