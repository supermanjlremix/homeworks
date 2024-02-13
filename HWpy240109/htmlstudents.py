def get_html_students(data_students: tuple, course: str='HTML') -> tuple:
    html_top_students = tuple(
        map(lambda student: student['name'],
            filter(lambda student: student['course'] == course and 
                   student['average_grade'] > 11, data_students)
        )
    )
    return html_top_students

