def get_students_list(data_students: tuple) -> tuple:
    names = map(lambda student: student['name'], data_students)
    names = tuple(names)
    return names


