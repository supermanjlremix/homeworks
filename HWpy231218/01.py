def get_size_area(x, y=None):
    if y is None:
        y = x

    return x * y

print("Площадь равна:", get_size_area("2.4"))
print("Площадь равна:", get_size_area(2))