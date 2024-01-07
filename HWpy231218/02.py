def get_barrel_capacity(d, h):
    try:
        d = float(d)
        h = float(h)
    except ValueError:
        print("Введенное значение не является числом")
        exit()

    pi = 3.14
    barrel_capacity = pi * (d / 2) ** 2 * h / 1000
    return barrel_capacity

print("Вместимость бочки равна:", get_barrel_capacity("20",60.5), "л")