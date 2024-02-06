from random import randint

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
    return matrix


try:
    rows = int(input("Введите количество строк (N): "))
    columns = int(input("Введите количество столбцов (M): "))
except ValueError:
    print("Ошибка: Введите целые числа для размеров матрицы.")

matrix = create_random_matrix(rows, columns)
for row in matrix:
    print(" ".join(row))