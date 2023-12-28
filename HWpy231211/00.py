text = input("Введите текст для форматирования: ").strip()

list_format = text.split(" ")

space = ""
while space in list_format:
    list_format.remove(space)

list_format[0] = list_format[0].capitalize()
for i in range(len(list_format)-1):
    if list_format[i][-1] in ".!?":
        list_format[i+1] = list_format[i+1].capitalize()

try:
    width = int(input("Введите ширину строки: "))
except ValueError:
    print("Введите цифру для длины строк!")

string_list = []
string = "   "
for word in list_format:
    if len(string) + len(word) < width:
        string += " " + word
    else:
        string_list += [string]
        string = word
string_list += [string]

for row in string_list: #не могу сделать пробелы по очередности между словами и чтобы абзац не учитывал
    row = list(row)
    for symbol in row:
        if len(row) == width:
            break
        elif symbol == " ":
            row.insert(row.index(symbol), " ")
    string = "".join(row)
    print(string)

