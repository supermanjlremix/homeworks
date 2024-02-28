num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError as error:
    print(error)
    exit()

print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)

try:
    num1 / num2
except ZeroDivisionError as error:
    print(error)
    exit()
else:
    print(num1, "/", num2, "=", num1 / num2)