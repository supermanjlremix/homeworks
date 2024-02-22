number = input("Введите число: ")

try:
    shift = int(input("На сколько цифр сдвинуть число: "))
except Exception as error:
    print(error)
    exit()    
    
shifted_number = number[shift:] + number[:shift]
print(f"Результат сдвига: {shifted_number}")
