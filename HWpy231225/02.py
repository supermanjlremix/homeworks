def find_same_last_names(employees: list=[]) -> list:
    last_name_dict = {}
    result = []
    for employee in employees:
        if type(employee) is not str:
            return []
        first_name, last_name = employee.split()
        if last_name not in last_name_dict:
            last_name_dict[last_name] = []
        last_name_dict[last_name].append(first_name)
    for last_name, first_names in last_name_dict.items():
        if len(first_names) > 1:
            a = ''.join((last_name + ": ", ", ".join(first_names)))
            result.append(a)
    return result


def test_find_same_last_names():
    assert find_same_last_names(["Иван Петров", "Мария Иванова", "Алексей Петров"]) == ['Петров: Иван, Алексей']
    assert find_same_last_names(["Иван Петров", "Мария Иванова", "Екатерина Сидорова"]) == []
    assert find_same_last_names(["Мария Иванова", "Екатерина Сидорова", "Юлия Иванова", "Елена Сидорова"]) == ['Иванова: Мария, Юлия', 'Сидорова: Екатерина, Елена']
    assert find_same_last_names([1, 2, 3]) == []
    assert find_same_last_names([True]) == []
    assert find_same_last_names([]) == []
    assert find_same_last_names() == []

test_find_same_last_names()

employee_names = ["Иван Петров", "Мария Иванова", "Екатерина Сидорова", 
                  "Петр Иванов", "Юлия Иванова", "Елена Сидорова", "Екатерина Сидорова"]
print(find_same_last_names(employee_names))
