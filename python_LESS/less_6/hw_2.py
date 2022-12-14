#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д.
from random import randint
my_list = [randint(1,20) for i in range(0, 10)]
print(my_list)
def my_func(args):
    while len(args) != 0:
        if len(args) == 1:
            print(f"осталось одно число в списке - {args}")
            break
        result = args[0] * args[-1]
        del args[0]
        del args[-1]
        print(result)
print(my_func(my_list))