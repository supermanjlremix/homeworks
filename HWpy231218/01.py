def get_size_area(x, y=None):
    if y is None:
        y = x

    try:
        x = float(x)
        y = float(y)
        #VN: функция не должна заниматься преобразованием входных данных! Это задача того кто использует функцию
    except ValueError:
        print("Введенное значение не является числом")
        exit()
        #VN: то же замечание, что и к предыдущей задаче

    return x * y

print("Площадь равна:", get_size_area("2.4"))
print("Площадь равна:", get_size_area(2))