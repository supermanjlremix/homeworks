number = input("Введите число: ")

try:
    number = float(number)
except ValueError as error:
    print(error)
    exit()

count_divisions = 0

while number >= 50:
    number /= 2
    count_divisions += 1

print("Полученное число:", number)
print("Количество делений:", count_divisions)

