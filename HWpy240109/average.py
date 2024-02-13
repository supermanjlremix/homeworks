from functools import reduce

def get_average_age(data_students: tuple) -> float:
    total_age = reduce(
        lambda acc, student: acc + student["age"], data_students, 0
    )
    average_age = total_age / len(data_students)
    return average_age


def get_average_python(data_students: tuple, course: str='Python') -> float:
    python_students = filter(
        lambda student: student["course"] == course, data_students)
    python_students_number = len(
        list(
            filter(
                lambda student: student["course"] == course, 
                data_students)
        )
    )
    total_grade_python = reduce(
        lambda acc, student: acc + student["average_grade"], 
        python_students, 0)
    average_grade_python = total_grade_python / python_students_number
    return average_grade_python


