def get_sum(numbers: list|tuple) -> float|int:
    sums = 0
    for number in numbers:
        sums += number
    return sums


# def get_mul2(num1, num2):
#     return num1 * num2

get_mul2 = lambda a, b: a * b



print(__name__)
