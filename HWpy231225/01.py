def find_distance(numbers: list=[]) -> int:
    if type(numbers) is not list or not numbers:
        return 0
    for number in numbers:
        if not type(number) in (int, float):
            return 0
    max_length = 1
    current_length = 1
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length


def test_find_distance():
    assert find_distance([4, 5, 5, 6, 7, 7]) == 6
    assert find_distance([4.5, 1, 2, 3, 4]) == 4
    assert find_distance([1, 2, 3, 1, 2, 3, 4]) == 4
    assert find_distance([3, 2, 1]) == 1
    assert find_distance([3, 2, '1']) == 0
    assert find_distance((3, 2, 1)) == 0
    assert find_distance(True) == 0
    assert find_distance(False) == 0
    assert find_distance([True]) == 0
    assert find_distance([]) == 0
    assert find_distance() == 0


test_find_distance()

user_numbers = [12, 3, 42, 4, 5, 5, 6, 7, 7]
result = find_distance(user_numbers)
print("Максимальная длина последовательности неубывающих чисел:", result)
