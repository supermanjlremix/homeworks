def create_matrix(rows, columns):
    """
    Создает прямоугольную матрицу размера 
    rows на columns, состоящую из нулей.
    """
    matrix = [[0] * columns for i in range(rows)]
    return matrix


try:
    rows = int(input("Введите количество строк (N): "))
    columns = int(input("Введите количество столбцов (M): "))
except ValueError:
    print("Введите целые числа для размеров матрицы")

matrix = create_matrix(rows, columns)
for row in matrix:
    print(" ".join(map(str, row)))
