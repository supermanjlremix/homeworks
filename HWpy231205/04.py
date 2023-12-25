"""5. В массива хранятся имена сотрудников, которым была выписана премия за месяц. Проверить, не попал ли кто-либо из сотрудников в эту базу дважды. 
Вывести имена этих наглецов)"""

try:
    user_list1 = input("Введите имена сотрудников, которым была выписана премия за месяц через запятую: ").split(",")
    user_list2 = []
    user_list1 = [name.strip() for name in user_list1]   

    for name in user_list1:
        if user_list1.count(name) > 1 and name not in user_list2:
            user_list2 += [name]
    if len(user_list2) != 0:
        print("Список мошенников:", ", ".join(user_list2))
        exit()
    else:
        print("Все сотрудники честные!")
        exit()
    
except Exception:
    print("Непредвиденная ошибка!")