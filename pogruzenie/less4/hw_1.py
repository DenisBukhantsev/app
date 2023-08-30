#задача 1    Напишите функцию для транспонирования матрицы
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def trans_matrix(args):
    trans = [[args[j][i] for j in range(len(args))] for i in range(len(args[0]))]
   
    return trans
print(trans_matrix(matrix))
