number = input("Введите пятизначное число: ")

try:
    number = int(number)
except ValueError as error:
    print(error)
    exit()

last_digit = number % 10
number = number // 10
number = last_digit * 10000 + number
print("Число с перемещенной последней цифрой в начало:", number)
