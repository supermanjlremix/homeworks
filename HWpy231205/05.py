""" **6** Тимур решил как-то отобразить в тексте BACKSPACE (т.е. удаление последнего символа). Он подумал, что символ `@` отлично для этого подходит. 
Всем своим знакомым он дал строки такого вида (например, `гр@оо@лк@оц@ва`), чтобы посмотреть, кому удастся написать программу, которая очищает 
строки от лишнего и печатает их в чистом виде (например, `голова`). Напишите такую программу."""

while True:
    try:
        sentence = input("Введите предложение: ")
        key = "@"
        symbols_list = []

        for symbol in sentence:
            if sentence[0] == key:
                sentence = sentence[1:]
            else:
                symbols_list += symbol

        for symbol in symbols_list:
            if symbol == key:
                symbols_list.pop(symbols_list.index(symbol)-1)
                symbols_list.pop(symbols_list.index(symbol))

        result = ""
        for symbol in symbols_list:
            result += symbol

        if len(result) == 0:
            print("Ваш результат пустая строка")
            exit()
        else:
            print("Результат:", result)
            exit()

    except Exception:
        print("Непредвиденная ошибка")