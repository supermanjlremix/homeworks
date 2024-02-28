import math

x1 = input("Введите координату x для первой точки: ")
y1 = input("Введите координату y для первой точки: ")
x2 = input("Введите координату x для второй точки: ")
y2 = input("Введите координату y для второй точки: ")

try:
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
except ValueError as error:
    print(error)
    exit()

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Расстояние между двумя точками:", distance)
