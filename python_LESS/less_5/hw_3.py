field_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
def field_show():
    print("------------------")
    print(f"    {field_list[0]}    {field_list[1]}    {field_list[2]}")
    print(f"    {field_list[3]}    {field_list[4]}    {field_list[5]}")
    print(f"    {field_list[6]}    {field_list[7]}    {field_list[8]}")
    print("------------------")

def player1game():
    wniner = "игрок 1 победил !"
    global field_list
    global choise
    x = False
    while x != True:
        field_show()
        choise = int(input("Игрок 1 вы ходите Х , ваш ход, выберите поле "))
        if field_list[choise] != "X" and field_list != "O":
            field_list[choise] = "X"
            field_show()
            x = True
            
        else:
            print(f"Это поле занято. попробуйте снова")
    win_combo = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    win_chek = False
    for i in win_combo:
        if field_list[i[0]] == field_list[i[1]] == field_list[i[2]]:
            print(wniner)
            win_chek = True
    if win_chek == False:
        player2game()

    field_show
def player2game():
    global field_list
    global choise
    wniner = "игрок 2 победил !"
    y = False
    while y != True:
        choise = int(input("Игрок 2 вы ходите O , ваш ход, выберите поле "))
        if field_list[choise] != "X" and field_list != "O":
            field_list[choise] = "O"
            field_show
            y = True
        else:
            print("Это поле занято. попробуйте снова " )
    win_combo = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    win_chek = False
    for i in win_combo:
        if field_list[i[0]] == field_list[i[1]] == field_list[i[2]]:
            print(wniner)
            win_chek = True
    if win_chek == False:
        player1game()
    field_show
print(player1game())
