# 2.	В списке найти минимальный и максимальный элементы, поменять их местами.

while True:
    try:
        user_list = input("Введите числа через запятую для создания списка: ").split(",")
        user_list = [float(number) for number in user_list]
        if len(user_list) < 2:
            print("Введите хотя бы 2 цифры!")
        else:
            max_index = user_list.index(max(user_list))
            min_index = user_list.index(min(user_list))

            max_number = user_list.pop(max_index)
            user_list.insert(min_index, max_number)
            min_index = user_list.index(min(user_list))
            min_number = user_list.pop(min_index)
            user_list.insert(max_index, min_number)

            print(user_list)
            exit()
    except ValueError:
            print("Введите только числа!")