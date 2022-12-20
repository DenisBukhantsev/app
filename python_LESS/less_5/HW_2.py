#2- Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому 
#игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint
candy = 2021
player1 = 0
taked1 = 0
player2 = 0
taked2 = 0
name = input("Введите имя игрока 1 ")
name2 = input("Введите имя игрока 2 ")
def shoiseplayer():
    random_num = randint(1,2)
    if random_num == 1:
        print(f"Жребий пал на {name}")
        player1game()
    else:
         print(f"Жребий пал на {name2}")
         player2game()
def player1game():
    global candy
    global taked1
    global player1
    global taked2
    global player2
    print(f"игрок {name} делает ход. \nСейчас на столе лежит {candy} конфет")
    taked1 = int(input("сколько вы хотите взять конфет?"))
    while taked1 > 28 or taked1 < 0 or taked1 > candy:
        taked1 = int(input("неверный ввод введи колличество по условиям игры "))
    candy -= taked1
    player1 += taked1
    print(f"игрок {name} взял {taked1} конфет")
    if candy > 0:
        player2game()
    else:
        print(f" {name} вы победили!\n Общий счет составил {name} : {player1} конфета и {name2} : {player2} конфет")
        print(f"так как вы были последним вы забираете все оставшиеся конфеты у {name2} и теперь у вас {player1 + player2} конфет")

def player2game():
    global candy
    global taked2
    global player2
    global taked1
    global player1
    print(f" игрок {name2} делает ход. \nСейчас на столе лежит {candy} конфет")
    taked2 = int(input("сколько вы хотите взять конфет?" ))
    while taked2 > 28 or taked2 < 0 or taked2 > candy:
        taked2 = int(input("неверный ввод введи колличество по условиям игры "))
    candy -= taked2
    player2 += taked2
    print(f"игрок {name2} взял {taked2} конфет")
    if candy > 0:
        player1game()
    else:
        print(f" {name2} вы победили!\n Общий счет составил {name2} : {player2} конфета и {name} : {player1} конфет")
        print(f"так как вы были последним вы забираете все оставшиеся конфеты у {name}  и теперь у вас {player2 + player1} конфета!!!")
print(shoiseplayer())
