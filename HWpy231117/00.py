decimal_number = input("Введите десятичное число: ")

try:
    decimal_number = int(decimal_number)
except ValueError as error:
    print(error)
    exit()

binary_number = bin(decimal_number)
octal_number = oct(decimal_number)
hexadecimal_number = hex(decimal_number)

print("Двоичное представление:", binary_number)
print("Восьмеричное представление:", octal_number)
print("Шестнадцатеричное представление:", hexadecimal_number)
