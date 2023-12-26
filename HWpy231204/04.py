# 5. Создать строку длины N, которая состоит из чередующихся символов C1 и C2, начиная с C1.


try:
    length = int(input("Введите длину: "))
except ValueError:
    print("Введите число для длины строки! Попробуйте снова")
    exit()


first_symbol = input("Введите первый символ: ")
second_symbol = input("Введите второй символ: ")

all_symbols = first_symbol + second_symbol
word = all_symbols * length
text = "%.*s"
print("Результат:", text % (length, word))
