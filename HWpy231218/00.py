def get_sum_numbers(number1, number2, number3):
    result = str(number1) + str(number2) + str(number3)
    return result


number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
number3 = input("Введите третье число: ")

try:
    number1 = int(number1)
    number2 = int(number2)
    number3 = int(number3)
except ValueError:
    print("Значение нельзя преобразовать в число")
    exit()

print("Результат:", get_sum_numbers(number1, number2, number3))
