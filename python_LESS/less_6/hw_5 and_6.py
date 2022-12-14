#Задача 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при 
# условии, что они не совпадают.
#[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)] 

from random import randint
random_list = [randint(1,100) for i in range(0, 200)]
#print(random_list) # создали список 
#print(len(random_list)) # проверка длинны 

def answer_fuc(args):
    global answer
    #random_list = [1, 2, 3, 6, 7, 10, 12, 5, 43, 76]
    answer = [(i, el) for i, el in enumerate(args) if i != el]
    return answer

print(f"создаем список кортежей по условиям задачи 5 : {answer_fuc(random_list)}") # проверяем работоспособность функции по задаче № 5
# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
#Пример
#[(10,25),(3,4),(4,1)] => [(10,25),(4,1)]
def answer2_func(args):
    answer2 = [i for i in answer if sum(i) % 5 == 0]
    return  answer2
print(f"пары, где сумма кортежа кратна 5:  {answer2_func(answer)}")
