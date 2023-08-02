#Задача 3 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
#должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
#числа используйте код:

def game_1():
    from random import randint
    number = randint(0, 1000)
    count = 10
   # print(number)  #для проверки можно принтить загаданное число

    while count != 0:
        user_num = int(input("попробуй отгадать число от 1 до 1000  "))
        if number < user_num:
            count -= 1
            print(f"ты не угадал, загаданное число меньше, у тебя осталось {count} попыток ")
        elif number > user_num:
            count -= 1
            print(f"ты не угадал, загаданное число больше, у тебя осталось {count} попыток")
        else:
            print("ты угадал")
            break
        if count == 0:
            print("твои попытки кончились , пока")

def game_2():
    print("ладно. давай я отгадаю твое число за 10 попыток")
    from random import randint
    count = 0
    num_list = [i for i in range(0, 1001)]
    low = min(num_list)
    high = max(num_list)
    answer = ""
    while count != 10:
        mid = (low + high) // 2
        answer = int(input(f" загаданное число это {mid} ? \n да - 1 . нет - 2 "))
        if answer == 1:
            print(f"я угадал ! за {count} попыток ")
            break
        elif answer == 2 or answer != 1:
            count += 1
            question = int(input(f"загаданное число больше или меньше {mid} \n больше - 1 . меньше - 2 "))
            if question == 2:
                high = mid + 1

            else:
                low = mid - 1
        elif count == 10:
            print("я не угадал")
choose = int(input(" с помощью цифр выбери, ты будешь отгадывать число или программа ? \n 1 - ты . 2 - программа \n - "))
while choose != 1 and choose != 2:
    choose = int(input(" что не понятного  ? просто нажми или  \n 1 - ты . или  2 - программа \n - "))
if choose == 1:
    game_1()
elif choose == 2:
    game_2()


