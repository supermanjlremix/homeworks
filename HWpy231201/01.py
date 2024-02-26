def fibonacci(N: int) -> list:
    fib_sequence = [0, 1]
    for i in range(2, N):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence


try:
    N = int(input("Введите количество чисел Фибоначчи: "))
    #VN: input не нужен в try
except Exception as error:
    #VN: ^^^^^^^ неизбирательный обработчик может принести проблемы. Указывайте конкретное исключение, которое ловите
    print(error)
    exit()

fib_numbers = fibonacci(N)
for num in fib_numbers:
    print(num, end=" ")
