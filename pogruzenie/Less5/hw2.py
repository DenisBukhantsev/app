#Задача 2 Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
#премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
#как ставка умноженная на процент премии
name = ["denis", "maksim", "lera"]
stavka = [40000, 55000, 63000]
premm = ["10.25%", "11.30%", "12.00%"]
#less5dict = {key : val1 * (val1 // 100 * float(val2[0:len(val2) -1])) for key, val1, val2 in zip(name, stavka, premm)}   # с помощью метода зип обрабатываю три списка одновременно, и срезами беру из строки  c премииями только цифры без символа % и с помощью формурлы нахождения процента от числа добавляю в словарь уже посчитанную сумму 
print({key : val1 * (val1 // 100 * float(val2[0:len(val2) -1])) for key, val1, val2 in zip(name, stavka, premm)})
