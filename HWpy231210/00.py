try:
    source = [int(number) for number in input("Введите цифры через пробел: ").split()]
except ValueError:
    print("Введите цифры через пробел!")
    exit()

result = []
for number in source:
    if number == 0:
        result += [number]
    else:
        result += [int(number/abs(number))]
    
print(result)
