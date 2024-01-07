def get_sum_numbers(number=0):
    numbers = str(number)
    numbers = list(numbers)
    count = 0

    for number in numbers:
        try:
            count += int(number)
        except ValueError:
            print("Введенное значение не является целым числом")
            exit()

    return count

print("Сумма чисел равна:", get_sum_numbers("123"))