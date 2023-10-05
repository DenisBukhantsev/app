# Задание №1
#Создайте функцию, которая запрашивает числовые данные от
#пользователя до тех пор, пока он не введёт целое или
#вещественное число.
#Обрабатывайте не числовые данные как исключения
def input_number():
  while True:
    number = input("введите целое или вещественное :")
    try:
      return int(number)
    except:
      try:
        return float(number)
      except:
        print("это не число, еще раз !")
    
  
#print(input_number())
# ЗАдание 2 Создайте функцию аналог get для словаря.
#Помимо самого словаря функция принимает ключ и
#значение по умолчанию.
#При обращении к несуществующему ключу функция должна
#возвращать дефолтное значение.
#Реализуйте работу через обработку исключений.

from typing import Any
dict_1 = {1: "one", 2: "two"}
def my_dict_get(dct: dict, key: Any, default_value: Any = None) -> Any:
  try:
    return dct[key]
  except KeyError:
    return default_value
  except TypeError:
    return "ошибка типа ключа "
print(my_dict_get(dict_1, 2))
print(my_dict_get(dict_1, 1))
print(my_dict_get(dict_1, [1, 2]))
