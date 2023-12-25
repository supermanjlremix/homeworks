try:
    input_str = input("Введите предложение: ")
    step = int(input("Введите число для шага: "))

    max_en = ord("z") - ord("a") 
    min_step_en = step % (max_en+1) 
    max_ru = ord("я") - ord("а") 
    min_step_ru = step % (max_ru+1) 


    output_str = ""

    for letter in input_str:
        if "A" <= letter.upper() <= "Z":
            if ord(letter.upper()) + min_step_en <= ord("Z"): 
                letter = chr(ord(letter) + min_step_en) #Если ord() заменяющей буквы находится в диапазоне
                output_str += letter
            else: 
                letter = chr(ord(letter) + min_step_en - max_en - 1) #Если ord() заменяющей буквы находится вне диапазона
                output_str += letter
        elif "А" <= letter.upper() <= "Я":
            if ord(letter.upper()) + min_step_ru <= ord("Я"): 
                letter = chr(ord(letter) + min_step_ru) #Если ord() заменяющей буквы находится в диапазоне
                output_str += letter
            else: 
                letter = chr(ord(letter) + min_step_ru - max_ru - 1) #Если ord() заменяющей буквы находится вне диапазона
                output_str += letter
        else:
            output_str += letter
    print("Результат:", output_str)
    exit()
except ValueError:
    print("Введите целое число для шага!")
