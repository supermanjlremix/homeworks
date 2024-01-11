def get_size_area(x: int|float, y:int|float=None) -> int|float:
    if y == None:
        y = x
    size_area = x * y
    return size_area


print("Площадь равна:", get_size_area(2, 5))
print("Площадь равна:", get_size_area(2.4))
