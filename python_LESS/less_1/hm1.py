# урок 1 задача 1 
number = int(input("Введите число обозначающее день недели - "))
while number > 7:
    print("ты ввел неверное число, в неделе только 7 дней")
    number = int(input("Введите число обозначающее день недели - "))
if number == 6 or number == 7:
    print("да, этот день выходной")
elif number > 7:
    print("В неделе только 7 дней")
else:
    print("нет, этот день не выходной")