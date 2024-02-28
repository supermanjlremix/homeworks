def find_local_extremes(temperatures: list=[]) -> str:
    local_minima = []
    local_maxima = []
    for temperature in temperatures:
        if not type(temperature) in (int, float):
            return "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    for i in range(1, len(temperatures) - 1):
        if temperatures[i] < temperatures[i - 1] and temperatures[i] < temperatures[i + 1]:
            local_minima.append((i + 1, temperatures[i]))
        elif temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            local_maxima.append((i + 1, temperatures[i]))
    minimum = maximum = []
    for day, temp in local_minima:
        minimum.append(f"день {day} - {temp}°")
    if len(minimum) > 1:
        text_min = "Минимумы: " + ", ".join(minimum)
    else:
        text_min = "Минимумы: таких дней нет"
    for day, temp in local_maxima:
        maximum.append(f"день {day} - {temp}°")
    if len(minimum) > 1:
        text_max = "Максимумы: " + ", ".join(maximum)
    else:
        text_max = "Максимумы: таких дней нет"
    text_all = "\n".join([text_min, text_max])
    return text_all


def test_find_local_extremes():
    assert find_local_extremes([23, 21, 18, 15, 18, 16, 17, 19, 22, 25, 23, 21, 18, 15]) == 'Минимумы: день 4 - 15°, день 6 - 16°\nМаксимумы: день 4 - 15°, день 6 - 16°, день 5 - 18°, день 10 - 25°'
    assert find_local_extremes([16, 17, 19, 22, 25, 23]) == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    assert find_local_extremes([22, 25, 23, 21, 18, 15, 18, 16, 17, 19, 22, 25, 23, 2]) == "Минимумы: день 6 - 15°, день 8 - 16°\nМаксимумы: день 6 - 15°, день 8 - 16°, день 2 - 25°, день 7 - 18°, день 12 - 25°"
    assert find_local_extremes([20]) == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    assert find_local_extremes([1, 2, 3]) == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    assert find_local_extremes([False, True, False, True, False, True, False]) == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    assert find_local_extremes([]) == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"
    assert find_local_extremes() == "Минимумы: таких дней нет\nМаксимумы: таких дней нет"

test_find_local_extremes()

temperatures = [20, 18, 16, 17, 19, 22, 25, 23, 21, 18, 15, 18, 16, 17, 19, 22, 25, 23, 21, 18, 15, 18, 16, 17, 19, 22, 25, 23, 21, 18, 15]
print(find_local_extremes(temperatures))

