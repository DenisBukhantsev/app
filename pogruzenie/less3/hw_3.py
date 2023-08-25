# задача 3 оздайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
things = {"топор" : 4, "спальник" : 2, "горелка" : 3}
#print(things)
maxbag = int(input("масса рюкзака = "))
new_things = list(things.items())
values = []
#print(new_things)
for name, mass in new_things:
    if maxbag > mass and sum(values) < maxbag:
        values.append(mass)
    if sum(values) > maxbag:
        break

#print(values)
print("влезет")
for i, y in new_things:
    if y in values:
        print(f' {i} , {y} кг')
