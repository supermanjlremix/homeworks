def get_sum_numbers(number=0):
    numbers = str(number)
    numbers = list(numbers)
    count = 0

    for number in numbers:
        count += int(number)


    return count

print("Сумма чисел равна:", get_sum_numbers("123"))

#VN: Не выполнено условие: Написать функцию, которая принимает три отдельные цифры...
# т.е. вызов вашей функции должен быть такой: get_sum_numbers(1, 2, 3), а результатом - число 123