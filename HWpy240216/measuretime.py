import time
from functools import wraps
from random import randint

def measuretime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"{func.__name__}() - {execution_time_ms:.2f} мс")
        return result
    return wrapper

@measuretime
def create_random_matrix(rows, columns):
    """
    Создает прямоугольную матрицу размера rows на columns,
    состоящую из случайных чисел от -20 до 20.
    """
    matrix = [[str(randint(-20, 20)) 
               for i in range(columns)] for i in range(rows)]
    for row in matrix:
        for i in range(len(row)):
            if len(row[i]) == 3:
                continue
            elif len(row[i]) > 1:
                row[i] = " " + row[i]
            else:
                row[i] = "  " + row[i]   
    time.sleep(0.1)     
    return matrix
    
rows = input("Введите количество строк (N): ")
columns = input("Введите количество столбцов (M): ")
try:
    rows = int(rows)
    columns = int(columns)
except ValueError:
    print("Ошибка: Введите целые числа для размеров матрицы.")
    exit()

matrix = create_random_matrix(rows, columns)
for row in matrix:
    print(" ".join(row))