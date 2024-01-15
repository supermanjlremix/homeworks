try:
    my_file = open("input.txt", "r", encoding="utf8") 
    input_text = my_file.read()
except FileNotFoundError:
    print("File Not Found Error")
finally:
    my_file.close()

user_list = input_text.split()

for word in user_list:
    if "$" in word or "USD" in word:
        price = user_list[user_list.index(word)-1]
        try:
            price = float(price)
        except ValueError:
            print("!")
            exit()       
        user_list[user_list.index(word)-1] = str(500 * price)
        user_list[user_list.index(word)] = word.replace("$", "₸").replace("USD", "₸")
    if "€" in word or "EUR" in word:
        price = user_list[user_list.index(word)-1]
        try:
            price = float(price)
        except ValueError:
            print("!")
            exit()       
        user_list[user_list.index(word)-1] = str(550 * price)
        user_list[user_list.index(word)] = word.replace("€", "₸").replace("EUR", "₸")

output_text = " ".join(user_list)

try:    
    my_file = open('output.txt','w', encoding="utf8")  
    my_file.write(output_text)
except PermissionError:
    print("Permission denied") 
finally:
    my_file.close()
