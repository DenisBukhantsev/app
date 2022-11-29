people = input("Введите имена игроков через пробел " ).split()
def game(people):
    mydict = dict.fromkeys(people, 0)
    print(mydict)
    from random import randrange
    while len(mydict) != 1:
        index = randrange(0, len(mydict))
        print(f"Ведущий выбрал игрока {people[index]}")
        for i in range(0, len(mydict)):
            if i < index:
                mydict[people[i]] = mydict[people[i]] + 1
            else:
                mydict[people[i]] = mydict[people[i]] + 2
        if index == len(mydict) or index == len(mydict) - 1:
            mydict[people[0]] = mydict[people[0]] + mydict[people[index]]
        else:
            mydict[people[index +1]] = mydict[people[index + 1]] + mydict[people[index]]
        print(f'Игрок {people[index]} выбывает')
        question = input("продолжаем дальше? " )
        if question == "нет"or question == "no":
            print(mydict)
            break
        
        del mydict[people[index]]
        del people[index]
        print(mydict)
#print(mydict)
game(people)