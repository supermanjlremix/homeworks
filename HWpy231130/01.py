num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError as error:
    print(error)
    exit()

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

print("Наибольший общий делитель чисел:", num1)
