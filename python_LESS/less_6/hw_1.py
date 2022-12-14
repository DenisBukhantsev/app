#задача 1 Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
my_list = ["qwe", "asd", "zxc", "qwerty", "qwe"]
my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] # ищем: "йцу", ответ: 5
my_list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #ищем: "йцу", ответ: -1
my_list4 = ["123", "234", 123, "567"] #ищем: "123", #ответ: -1
my_list5 = [] # ищем: "123", ответ: -1
def search_words(args):
    res = [i for i, el in enumerate(args) if args.count(el) == 2]
    if len(res) > 0:
        res.pop(0)
        return res
    else:
        return print("второго вхождения нет")

    

print(search_words(my_list2))
