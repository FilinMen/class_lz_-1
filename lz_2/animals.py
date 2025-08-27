import math
# parent's class
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    # function make_sound
    def make_sound(self):
        print(f"{self.name} издает звук!")

    def info(self):
        print(f"Имя- {self.name}")
        print(f"Возраст- {self.age} ")
        print(f"Вид- {self.species}")

    def __del__(self):
        print(f"Объект {self.name} был удален")


class Dog(Animal):
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species)
        self.breed = breed
        

    def info(self):
        super().info()
        print(f"Порода: {self.breed}")
        print(f"{self.name} охраняет дом! Гав-гав!")
        

    def __del__(self):
        print(f"Объект {self.name} удален")
        
