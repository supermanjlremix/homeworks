try:
    my_file = open("urls.txt", "r") 
    url_list = my_file.readlines()
except FileNotFoundError:
    print("File Not Found Error")
finally:
    my_file.close()

for url_address in url_list:
    print("--------------------------------------------------------")
    protocol = ""
    for symbol in url_address:
        if symbol == ":":
            url_address = url_address[url_address.index(symbol)+3:]
            break
        protocol += symbol
    print("Протокол:", protocol)

    domen_name = ""
    for symbol in url_address:
        if symbol == "/":
            url_address = url_address[url_address.index(symbol):]
            break
        domen_name += symbol
    print("Доменное имя:", domen_name)

    request = ""
    for symbol in url_address:
        if symbol == "?":
            url_address = url_address[url_address.index(symbol)+1:]
            break
        request += symbol
    print("Запрос:", request)

    print("Параметры:")
    options = ""
    for symbol in url_address:
        if symbol == "&":
            print("\t", options)
            options = ""
            url_address = url_address[url_address.index(symbol)+1:]
            continue
        options += symbol

