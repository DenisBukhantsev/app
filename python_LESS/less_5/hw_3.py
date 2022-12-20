field_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
def field_show():
    print("------------------")
    print(f"    {field_list[0]}    {field_list[1]}    {field_list[2]}")
    print(f"    {field_list[3]}    {field_list[4]}    {field_list[5]}")
    print(f"    {field_list[6]}    {field_list[7]}    {field_list[8]}")
    print("------------------")

def player1game():
    wnin = "игрок 1 победил !"
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
    if field_list[0] == "X" and field_list[3] == "X" and field_list[6] == "X":
        print(wnin)
    elif field_list[1] == "X" and field_list[4] == "X" and field_list[7] == "X":
        print(wnin)
    elif field_list[2] == "X" and field_list[5] == "X" and field_list[8] == "X":
        print(wnin)
    elif field_list[0] == "X" and field_list[4] == "X" and field_list[8] == "X":
        print(wnin)
    elif field_list[2] == "X" and field_list[4] == "X" and field_list[6] == "X":
        print(wnin)
    else:
        player2game()
    field_show
def player2game():
    global field_list
    global choise
    wnin = "игрок 2 победил !"
    y = False
    while y != True:
        choise = int(input("Игрок 2 вы ходите O , ваш ход, выберите поле "))
        if field_list[choise] != "X" and field_list != "O":
            field_list[choise] = "O"
            field_show
            y = True
        else:
            print("Это поле занято. попробуйте снова " )
    if field_list[0] == "O" and field_list[3] == "O" and field_list[6] == "O":
        print(wnin)
    elif field_list[1] == "O" and field_list[4] == "O" and field_list[7] == "O":
        print(wnin)
    elif field_list[2] == "O" and field_list[5] == "O" and field_list[8] == "O":
        print(wnin)
    elif field_list[0] == "0" and field_list[4] == "O" and field_list[8] == "O":
        print(wnin)
    elif field_list[2] == "O" and field_list[4] == "O" and field_list[6] == "O":
        print(wnin)
        
    else:
        player1game()
    field_show
print(player1game())
