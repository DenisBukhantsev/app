#2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]
numbers_1 = [2, 3, 5, 6]
result = []
while len(numbers_1) != 0:
    item = numbers_1[0] * numbers_1[-1]
    result.append(item)
    del numbers_1[0]
    if len(numbers_1) == 0:
        break
    del numbers_1[-1]
print(result)