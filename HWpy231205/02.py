# 3.	Создать два списка. Удалить из первого списка такие элементы, которые есть во втором списке.

user_list1 = input("Введите слово или число через запятую для первого списка: ").split(",")
user_list2 = input("Введите слово или число через запятую для второго списка: ").split(",")
user_list3 = []

for x in user_list1:
    if x in user_list2:
        user_list3 += [x]

for y in user_list3:
    user_list1.remove(y)

print("Результат:", ", ".join(user_list1))




