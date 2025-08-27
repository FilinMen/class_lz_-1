class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def info(self):
        print('Кличка', self.name)
        print('Возраст', self.age)
        print('Вид', self.species)

    def __del__(self):
        print('Delete')


class Dog(Animal):
    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status.lower() in ['true']

    def info(self):
        super().info()
        print('Порода', self.breed)
        print('Статус охранника:', 'Да' if self.guard_status else 'Нет')

    def guard_house(self):
        if self.guard_status:
            print(f"{self.name} охраняет дом")
        else:
            print(f"{self.name} не охраняет дом")