#Задача 1

a = "https://gbcdn.mrgcdn.ru/uploads/asset/4920276/attachment/7e1accab32ccfc3a8095d79a4597cb86.pdf"
b = "https://github.com/DenisBukhantsev/app/blob/main/pogruzenie/less4/hw_1.py"
#print(a)
#print(b)
def funcmy(args):
    args = args.split('/')   # делим строку на список по слешам 
    new_a = args[-1].split('.') #создаем переменную куда кладем уже из списка аргс последним элемент и разбиваем его по точке  на имя и тип 
    mytuple = ("/".join(args), new_a[0], new_a[1]) #а здесь создаем кортеж  склеиваем путь обратно по слешам что бы смотрелся и добавляем имя и тип из второй переменной 
    return mytuple
    
print(funcmy(b)) # вроде все работает , возможно  я что то не понял и можно это сделаь как то с помощью генераторов, просто это первое что пришло в голову
