#Задача 1
number = float(input("напишите любое вещественное число "))
numbers = str(number)
result = []
for i in numbers:
    if i.isdigit():
        i = int(i)
        result.append(i)
print(f'сумма цифр числа {sum(result)}')

#Задача 2
n = int(input("Введите число "))
numbers = []
factorial = 1
 
for i in range(1, n+1):
    factorial *= i
    numbers.append(factorial)
 
print(f'набор произведений числа {n} \n {numbers}')