#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
def my_func2(**args):
    val = args.keys()
    key = args.values()
    result = {} #{str(x): y for x, y in zip(key, val)} это выражение в одну строку но тут все ключи будут str
    for x, y in zip(key, val):
        if type(x) != int:
            result[str(x)] = y 
        else:
            result[x] = y
    return result
print(my_func2(a = 2, w = "sdfs", goal = ["dsdf", "ваыва", 111]))
