def get_barrel_capacity(d, h):
    try:
        d = float(d)
        h = float(h)
        #VN: то же замечание, что и в 01.py
    except ValueError:
        print("Введенное значение не является числом")
        exit()
        #VN: тоже, что и в 00.py

    pi = 3.14
    barrel_capacity = pi * (d / 2) ** 2 * h / 1000
    return barrel_capacity

print("Вместимость бочки равна:", get_barrel_capacity("20",60.5), "л")
#VN: ошибка преобразования в литры: бак диаметром 20 метров и
# высотой 60.5 метров не может иметь объём всего 18.9 литров!
