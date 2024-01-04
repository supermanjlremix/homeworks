# 4.  Определить расстояние между минимальным и максимальным числами внутри массива.

try:
    user_list = [float(number) for number in input("Введите данные через запятую для создания списка: ").split(",")]
except ValueError:
    print("Введите цифры!")
    exit()
#VN: Нет выхода при возникновении исключения или ветки else

max_index = user_list.index(max(user_list))
min_index = user_list.index(min(user_list))
distance = abs(max_index - min_index)

print("Расстояние между минимальным и максимальным числами внутри массива:", distance)
