def syracuse_hypothesis(number: int) -> tuple[int, list]:
    result = []
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        iterations += 1
        result.append(number)
    return iterations, result


try:
    number = int(input("Введите натуральное число: "))
except Exception as error:
    print(error)
    exit()

iterations_count = syracuse_hypothesis(number)
print(f"Количество произведенных итераций: {iterations_count[0]}, значения: {iterations_count[1]}")
