def get_barrel_capacity(d: int|float, h:int|float) -> float:
    pi = 3.14
    barrel_capacity = ((h * 1000) * pi * (d * 1000) ** 2 / 4)  / 1000000
    return barrel_capacity


print("Вместимость бочки равна:", get_barrel_capacity(1, 2), "л")

