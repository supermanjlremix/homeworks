try:
    input_str = input("Введите предложение: ")
    step = 1
    output_str = ""
    max_ru = ord("я") - ord("а") 
    max_en = ord("z") - ord("a") 
    
    for letter in input_str:
        if letter == "ё": 
            output_str += "ж"
        elif letter == "е": 
            output_str += "ё"
        elif letter == "Ё": 
            output_str += "Ж"
        elif letter == "Е": 
            output_str += "Ё"
        elif letter.lower() == "я": 
            output_str += chr(ord(letter) - max_ru)
        elif letter.lower() == "z": 
            output_str += chr(ord(letter) - max_en)
        elif "a" <= letter.lower() < "z" or "а" <= letter.lower() < "я":
            output_str += chr(ord(letter) + step)
        else:
            output_str += letter
    print("Результат:", output_str)
    exit()
except Exception:
    print("Непредвиденная ошибка")