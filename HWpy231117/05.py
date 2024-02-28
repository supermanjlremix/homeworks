number = input("Введите трехзначное число: ")

try:
    number = int(number)
except ValueError as error:
    print(error)
    exit()

second_digit = (number % 100) // 10
print("Вторая цифра числа:", second_digit)
