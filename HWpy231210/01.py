try:
    source = [int(number) for number in input("Введите цифры через пробел: ").split()]
    result = []
    for number in source:
        k = 0
        for i in range(2, number // 2 + 1):
            if (number % i == 0):
                k = k+1
        if (k == 0):
            result += [number]
        
    print(result)
    exit()
except ValueError:
    print("Введите цифры через пробел!")