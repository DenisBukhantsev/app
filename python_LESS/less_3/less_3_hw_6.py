name = open("names")
money = open("cash")
result_dict = {}
for i in name.readlines():
    result_dict.setdefault(i.rstrip())
for i, key in enumerate(result_dict):
    result_dict[key] = float(money.readline())

print(result_dict)
coef = input("люба забыла про любимчиков босса и их клевый коэффицент, введи имена любимчиков  ").split(',')
for i in result_dict:
    if i in coef:
        result_dict[i] = result_dict[i] * 2
    else:
        result_dict[i] = result_dict[i] * 1.5
print(result_dict)