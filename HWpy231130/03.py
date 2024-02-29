positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0
total_numbers = 0

print("Введите 10 чисел:")
while total_numbers < 10:
    num = input()
    try:
        num = int(num)
    except ValueError as error:
        print(error)
        exit()
    total_numbers += 1

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)
print("Количество нулей:", zero_count)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
