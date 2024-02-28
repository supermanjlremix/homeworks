perimeter = input("Введите периметр квадрата: ")

try:
    perimeter = float(perimeter)
except ValueError as error:
    print(error)
    exit()

side_length = perimeter / 4
area = side_length ** 2
print("Площадь квадрата равна:", area)
