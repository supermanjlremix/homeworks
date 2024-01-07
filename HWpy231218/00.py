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
            #VN: функция не должна решать, завершать ли программу. это просто функция
            # print внутри функции - это тоже побочный эффект, он не нужен

    return count

print("Сумма чисел равна:", get_sum_numbers("123"))

#VN: Не выполнено условие: Написать функцию, которая принимает три отдельные цифры...
# т.е. вызов вашей функции должен быть такой: get_sum_numbers(1, 2, 3), а результатом - число 123