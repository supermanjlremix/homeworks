def get_names(numbers):
    result = []
    for digit in numbers:
        match digit:
            case 1:
                result += ["один"]
            case 2:
                result += ["два"]
            case 3:
                result += ["три"]
            case 4:
                result += ["четыре"]
            case 5:
                result += ["пять"]
            case 6:
                result += ["шесть"]
            case 7:
                result += ["семь"]
            case 8:
                result += ["восемь"]
            case 9:
                result += ["девять"]
            case 0:
                result += ["ноль"]
            case _:
                result += [""]
    if type(numbers) is tuple:
        result = tuple(result)
    return result


def test_get_names():
    assert get_names([3,5,1]) == ["три", "пять", "один"]
    assert get_names((3,11)) == ("три", "")
    assert get_names([]) == []
    print("Test ok")


test_get_names()