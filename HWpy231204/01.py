""" 2. Нумерология. Запросите у пользователя слово любой длины и выведите сумму кодов всех символов в этом слове. 
Для нахождения кода символа используйте функцию ord()."""


word = input("Введите слово или букву любой длины: ")

symbols_sum = 0
if len(word) == 0:
    print("Вы не ввели ни одной буквы! Попробуйте снова")
elif word.isalpha():
    for symbol in word:
        symbols_sum += ord(symbol)
    print("Сумма кодов всех символов вашего слова равна:", symbols_sum)
    exit()
else:
    print("Введите слово только из букв! Попробуйте снова")


