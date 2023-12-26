# 6. Запросить у пользователя слово и вывести его написание с большой буквы. Не использовать методы строк для этого!

word = input("Введите слово: ")

try:
    first_symbol_upper = chr((ord(word[0]) - (ord("a") -ord("A"))))
except IndexError:
    print("Вы не ввели ни одного символа! Попробуйте снова")
    exit()
except ValueError:
    print("Недопустимое значение! Попробуйте снова")
    exit()

print("Ваше слово с заглавной буквы:", first_symbol_upper + word[1:])