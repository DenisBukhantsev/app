#Урок 1 задача - Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#4-Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
x = int(input("Введите значение х- "))
y = int(input("Введите значение у- "))
if x > 0 and y > 0:
    result = 1
    print("диапазон точек х (0+) у (0+)")
elif x < 0 and y > 0:
    result = 2
    print("диапазон точек х (0-) у (0+)")
elif x < 0 and y < 0:
    result = 3
    print("диапазон точек х (0-) у (0-)")
elif x > 0 and y < 0:
    result = 4
    print("диапазон точек х (0+) у (0-)")
print(f"Точка находиться в  координатной четверти № {result} ")