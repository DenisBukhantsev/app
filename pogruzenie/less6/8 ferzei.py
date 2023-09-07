#feild = 
#[
#[0, 0, 0, 0, 0, 0, 0, 0], 
#[0, 0, F, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, F, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0],
#print(feild)
def chek1():
    # горизонтальная вертикальная проверка
    for ferz in mytuple:
        if feild1[ferz[0]].count("F") > 1:
            return print("ошибка по горизонтали")
        for i in feild1[ferz[0] + 1: ]:
            if i[ferz[1]] == "F":
                return print("по вертикали")
def chek2():
    for ferz in mytuple:
        for i in feild1[ferz[0]:]:
            if i[ferz[1]  + 1] == "F" or i[ferz[1]  - 1] == "F" :
                return "по диагонали"
        for y in feild1[ferz[0]::-1]:
            if i[ferz[1]  - 1] == "F"or  i[ferz[1]  + 1] == "F":
                return "по диагонали - "
            
        
feild1 = [[ "-" for j in range(8)] for i in range(8)]
counter = 3 

mytuple = [(int(input(f'введи кординат А ферзя {i} - ')), int(input(f'введи кординат b ферзя {i} - '))) for i in range(1, counter + 1)]
for i in mytuple:
    feild1[i[0]][i[1]] = "F"
print([print(i) for i in feild1])
print(chek1())
print(chek2())
