#1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
#Пример:
#Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок
def words_terminated(args):
    term = input("введите слова которые хотите удалить ").split()
    args = args.split(" ")
    new_args = [args.remove(i) for i in args if i in term]
    new_args = " ".join(map(str, args))
    return new_args
print(words_terminated("Конкретная функция, которую 5 вы хотите выполнить"))