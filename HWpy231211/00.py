text = input("Введите текст для форматирования: ").strip()
list_format = text.split(" ")

# - Удалить лишние пробелы между словами и в конце строк. / - Удалить лишние пустые строки.
space = "" 
while space in list_format:
    list_format.remove(space)

# - Исправить регистр символов - предложения должны начинаться с большой буквы.
try:
    list_format[0] = list_format[0].capitalize()
except IndexError:
    print("Вы не ввели ни одного символа")
    exit()
for i in range(len(list_format)-1):
    if list_format[i][-1] in ".!?":
        list_format[i+1] = list_format[i+1].capitalize()

try:
    width = int(input("Введите ширину строки: "))
except ValueError:
    print("Введите цифру для длины строк!")
    exit()

# - Разбить строки, длина которых превышает указанный размер, на более короткие строки, НЕ разрывая слова.
string_list = [] 
string = "   "
for word in list_format:
    if len(string) + len(word) < width:
        string += " " + word
    else:
        string_list += [string]
        string = word
string_list += [string]
if len(string_list) < 2:
    print(*string_list)
    exit()

# - Выровнять текст по ширине, чтобы каждая строка содержала одинаковое количество символов (при необходимости добавлять пробелы между словами), если только это не последняя строка.
for string in string_list:
    current_width = len(string.replace(" ", ""))
    if string == string_list[0]:
        current_width += 4
    num_spaces = width - current_width
    num_words = len(string.split()) - 1
    if num_words != 0:
        spaces = num_spaces // num_words
    
    # - Выделить начало абзаца - четырьмя пробелами.
    if string == string_list[0]: 
        new_string = "    "
    else:
        new_string = ""
    words = string.split()
    
    if string == string_list[-1]:
        print(string)
        break

    #- Вывести получившийся текст.
    try:
        for i in range(len(words) - 1):
            new_string += words[i] + " " * spaces
        new_string += words[-1]
    except IndexError:
        print("Указанная вами длина строк меньше возможного")
        exit()

    new_string = new_string.replace(" " * spaces, " " * spaces + " ", width - len(new_string))

    print(new_string) 

