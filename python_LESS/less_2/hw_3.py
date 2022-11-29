#3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
#Пример:
#- пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
#numbers = [int(i) for i in input('Введите цифры ').split()]  #Если хотим заполнить список сами
size = int(input("введите максимальный размер списка "))
from random import randint
numbers = [randint(-100, 100) for x in range(1, size)]
print(f"получили рандомный список чисел {numbers}")
result = []
for i in numbers:
    if i < 0:
        result.append(i)
        result.append(0)
    else:
        result.append(i)
print(f'итоговый список {result}')
