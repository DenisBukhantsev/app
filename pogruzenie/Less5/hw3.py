# Задача 3 Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fibonacci(n):
    a, b = 0, 1   #задачем стартовые значения в переменные 
    for i in range(n):
        a, b = b, a + b  # и в повторяющимся цикле меняем значения переменных местами и плюсуем к сохраненной в yield  а 
        yield a   # запоминаем значение в переменной а 
print(*fibonacci(10))