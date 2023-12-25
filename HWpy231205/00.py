""" 1.	Вывести элементы числового списка, которые больше, чем элементы, стоящие перед ними. Например, для списка [3, 9, 8, 4, 5, 1] следует вывести числа 
9 и 5, так как перед ними стоят соответственно числа 3 и 4, которые меньше их."""

result = []
while True:
    try:
        user_list = input("Введите числа через запятую: ").split(",")
        user_list = [float(number) for number in user_list]
        if len(user_list) < 2:
            print("Введите хотя бы 2 цифры!")
        else:
            for i in range(1, len(user_list)):
                if user_list[i] > user_list[i-1]:
                    result.append(user_list[i])  
            if len(result) > 0:
                print("Результат:", ', '.join(map(str, result)))
                exit()
            else:
                print("Нет соответствующих условиям чисел!")
                exit()
    except ValueError:
        print("Введите только числа!")


