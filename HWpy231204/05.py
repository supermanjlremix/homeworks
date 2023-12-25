# 6. Запросить у пользователя слово и вывести его написание с большой буквы. Не использовать методы строк для этого!

while True:
    try:
        word = input("Введите слово: ")
        first_symbol_upper = chr((ord(word[0]) - (ord("a") -ord("A"))))
        print("Ваше слово с заглавной буквы:", first_symbol_upper + word[1:])
        exit()
    except IndexError:
        print("Вы не ввели ни одного символа! Попробуйте снова")
    except ValueError:
        print("Недопустимое значение! Попробуйте снова")