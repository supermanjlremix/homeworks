text = input("Введите текст для форматирования: ").strip()

list_format = text.split(" ")

space = ""
while space in list_format:
    list_format.remove(space)

list_format[0] = list_format[0].capitalize()
for i in range(len(list_format)-1):
    if list_format[i][-1] in ".!?":
        list_format[i+1] = list_format[i+1].capitalize()

width = int(input("Введите ширину строки: "))
string_list = []
string = "   "
for word in list_format:
    if len(string) + len(word) < width:
        string += " " + word
    else:
        string_list += [string]
        string = word
string_list += [string]

for row in string_list:
    row = list(row)
    print(row, len(row))
    for symbol in row:
        if len(row) == width:
            break
        elif symbol == " ":
            row.insert(row.index(symbol), " ")
    string = "".join(row)
    print(string)
    print(row, len(row))

    # for symbol in row:
    #     spacer = " "
    #     if len(row) == width:
    #         break
    #     elif symbol == spacer and row[row.index(symbol)-1] != " ":
    #         # while len(row) != width or "  " in row:
    #         row = list(row)
    #         row.insert(row.index(symbol),spacer)
    #         print(row, len(row))

                # row = row[:row.index(symbol)]+ "  " + row[row.index(symbol)+1:]
    # string = "".join(row)
    # print(string)
    # print(row, len(row))




    # for symbol in row:
    #     if len(row) == width:
    #         break
    #     elif len(row) < width and symbol == " ":
    #         # row = row[:row.index(symbol)-1]+ "  " + row[row.index(symbol):]
    #         row = row.replace(" ", "  ")
    #         print(row, len(row))
