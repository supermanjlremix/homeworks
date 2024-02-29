import math

circumference_length = input("Введите длину окружности: ")
square_perimeter = input("Введите периметр квадрата: ")

try:
    circumference_length = float(circumference_length)
    square_perimeter = float(square_perimeter)
except ValueError as error:
    print(error)
    exit()

radius = circumference_length / (2 * math.pi)
circle_area = math.pi * radius ** 2
square_area = (square_perimeter / 4) ** 2
if circle_area <= square_area:
    print("Окружность может поместиться в указанный квадрат.")
else:
    print("Окружность не может поместиться в указанный квадрат.")
