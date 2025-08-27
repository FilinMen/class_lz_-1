# задание 8
import math

class Player:
    def __init__(self, name, level, experience, add_exp):
        self.name = name
        self.level = level
        self.experience = experience
        self.add_exp = add_exp


    def gain_experience(self):
        
        self.gain = self.experience + self.add_exp
        print(exp[self.level - 1])
        print(self.gain)
        while self.level < len(exp)  and self.gain >= int(exp[self.level - 1]):
            self.level += 1
        print('level up!!! Your level' ,self.level)

    """
    def show_stars(self):
        print('Имя', self.name)
        print('Уровень', self.level)
        print('Изначальный опыт игрока', self.experience)
        print('Текущий опыт игрока', self.gain)
    """ 


    

    def __del__(self):
        print('del')


class Warrior(Player):
    
    def __init__(self, name, level, experience, add_exp, weapon, armor):

        super().__init__(name, level, experience, add_exp)
        self.weapon = weapon
        self.armor = armor

    def attack(self):

        self.punch = (self.level/2) * self.weapon 
        print('Урон от атаки', self.punch)

    def defend(self):

        self.arm = math.log(self.experience)*self.armor
        print("Прочность защиты от атаки", self.arm)

    def show_stats(self):
        
        print('Имя:', self.name)
        self.gain = self.experience + self.add_exp
        while self.level < len(exp)  and self.gain >= int(exp[self.level - 1]):
            self.level += 1
        print('Ваш уровень:', self.level)
        print('Урон от атаки:', self.punch)
        print('Прочность защиты от атак:', self.arm)

    def __del__(self):
        print('del')

exp = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]

def main(): 

    name = str(input('Введите имя:'))
    level = int(input('Введите уровень 1-10:'))
    experience = int(input('Введите количество имеющегося опыта:'))
    add_exp = int(input('Введите количество доп опыта:'))
    weapon = int(input('Введите урон оружия:'))
    armor = int(input('Введите прочность защиты от атаки:'))


    player = Player(name, level, experience, add_exp)
    player.gain_experience()
    player = Warrior(name,level,experience,add_exp,weapon,armor)
    player.attack()
    player.defend()
    player.show_stats()

if __name__ == "__main__":
    main()