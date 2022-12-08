#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
#При расшифровке происходит обратная операция.
#К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
#считывает текст и дешифровывает его.

def cesar(args):
    result = []
    for el, in args:
        el =  ord(el) + 1
        el = chr(el)
        result.append(el)
    return "".join(result)
def del_cesar(args):
    result = []
    for el, in args:
        el =  ord(el) - 1
        el = chr(el)
        result.append(el)
    return "".join(result)
print(cesar('абаб'))
print(del_cesar("бвбв"))