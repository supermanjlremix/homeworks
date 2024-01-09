array = ["Timur", "Almat", "Sergey", "Sasha"]

new_array = sorted(array, key=lambda a: len(a))
print(new_array)

result = filter(lambda x: len(x) > 8, array)

result = filter(lambda x: x[0] < "В", array)

print(list(result))