#Доработаем задания 5-6. Создайте класс-фабрику.
#Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def voice(self):
        return "barks"
    def action(self):
        return "eats"



class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def voice(self):
        return "Meow"
    def action(self):
        return "sleep"


class AnimalFabrica:
    def animal_generator(self, animal_type, name, breed, age):
        if animal_type.lower() == "cat":
            return Cat(name, breed, age)
        elif animal_type.lower() == "dog":
            return Dog(name, breed, age)
        else:
            raise ValueError("error")
        

factory = AnimalFabrica()

cat = factory.animal_generator("cat", "Larry", "home cat", 3)
dog = factory.animal_generator("dog", "johny", "Spaniel", 10)
#other = factory.animal_generator("bird", "johny", "Spaniel", 10) error

print(cat.voice())  
print(dog.voice())
print(dog.action())
print(cat.action())
