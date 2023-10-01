class Mymatrix:
    def __init__(self, matrix):
        # проверяем матрицу на правильность что все строки и столбцы ровные
        for i in matrix:
            if len(i) != len(matrix[0]):
                raise ValueError("блин все строки в матрице должны быть одинаковы по длинне комон")
            else:
                self.matrix = matrix

    def __add__(self, other):
        # складываем  матрицы
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('невозможно сложить разного размера матрицы')

        answer = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Mymatrix(answer)

    def __mul__(self, other):
        #умножаем
        if len(self.matrix) != len(other.matrix[0]):
            raise ValueError('невозможно умножить разного размера матрицы')
        res = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]

        return Mymatrix(res)

    def __str__(self):
        # вывод матрицы
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
matrix1 = Mymatrix([[1, 2], [4, 5]])
matrix2 = Mymatrix([[2, 3], [0, 1]])
fail_matrix = Mymatrix([[1, 2, 3], [2, 3, 4]])

print(f"матрица 1 \n{matrix1}")

print(f"матрица 2 \n{matrix2}")

print(f'сложение \n{matrix1 + matrix2}')


print(f'умножение \n{matrix1 * matrix2}')
#print(matrix1 + fail_matrix)
