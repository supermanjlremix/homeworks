# 5. Создать строку длины N, которая состоит из чередующихся символов C1 и C2, начиная с C1.

while True:
    try:
        length = int(input("Введите длину: "))

        first_symbol = input("Введите первый символ: ")
        second_symbol = input("Введите второй символ: ")
        if len(first_symbol) == 1 and len(second_symbol) == 1:
            all_symbols = first_symbol + second_symbol
            word = all_symbols * length
            text = "%.*s"
            print("Результат:", text % (length, word))
            exit()
        else:
            print("Введите по одному символу!")
    except ValueError:
        print("Введите число для длины строки! Попробуйте снова")