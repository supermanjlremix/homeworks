a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

try:
    x = -b / a
except ZeroDivisionError as error:
    print(error)
    exit()
else:    
    print("Значение x равно:", x)

