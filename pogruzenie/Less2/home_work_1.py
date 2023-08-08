# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

d = {x: y for x, y in zip([str(i) for i in range(10, 16)], ["a", "b", "c", "d", "e", "f"])} # с помощью  гугла ;) я решил сделать генератор словаря, для будущей замены чисел
#print(d)
number = int(input("введи число  "))
double_num = number
result = [] #тут мы создаем пустой список, что бы класть туда при проверке числа  а потом сплитовать их и перевернуть

while number != 0:
    booble = str(number % 16)
    if d.get(booble) != None:
        booble = d[booble]
    result.append(booble)
    number //= 16
    


print(f'0x{"".join(reversed(result))}')
print("Проверка функцией hex", hex(double_num))
