lst = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(round(max(new_lst) - min(new_lst),2))