import names
import htmlstudents
import average

data_students = (
    {'name': 'Gerrard', 'age': 25 ,
     'course': 'Python', 'average_grade': 4.78},
    {'name': 'Harrison', 'age': 21,
     'course': 'Python', 'average_grade': 9.78}, 
    {'name': 'Vardy', 'age': 26,
     'course': 'HTML', 'average_grade': 7.78},
    {'name': 'Barnes', 'age': 27, 
     'course': 'HTML', 'average_grade': 11.78},
    {'name': 'Gordon', 'age': 25, 
     'course': 'HTML', 'average_grade': 12.78}
    )

if __name__ == "__main__":
    print(names.get_students_list(data_students))
    print(htmlstudents.get_html_students(data_students))
    print("Cредний возраст всех студентов:", 
          average.get_average_age(data_students))
    print("Cредний балл всех студентов на курсе 'Python':", 
          average.get_average_python(data_students))

#VN: Неплохо, но раз уж такая пьянка пошла с модулями, то функции получились очень узкоспециализированные.
# Лучше было бы сделать, чтобы можно было вызывать их так:
#   average.get_average_grade(data_students, course='Python'))
# и так:
#   average.get_average_grade(data_students))
# И то же с htmlstudents:
#   get_students(data_students, course='Html'))
# или:
#   get_students(data_students, name='Barnes'))