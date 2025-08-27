class Creauters:
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


class Tiger(Creauters):
    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status

    def info(self):
        super().info()
        print('Порода', self.breed)
        print('Статус охранника', self.guard_status)

    def guard_house(self):
        pass
