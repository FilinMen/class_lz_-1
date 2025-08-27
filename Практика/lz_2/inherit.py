<<<<<<< HEAD
# Вариант 3. Наслелование классов

# Создание родительского класса
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

     # Функция "info" выводит все данные об объекте родительского класса
    def info(self):
        print('Имя сотрудника-', self.name)
        print('Должность -', self.position)
        print('Заработная плата -', self.salary)

    # Функция "calc_salary" вывод заработной платы
    def calc_salary(self):
        print('Введите размер суточной заработной платы для данной должности')
        position_salary_worked_days = int(input())
        print (position_salary_worked_days)

    # Создание наследственного класса "Manager"
class Manager(Employee):
    def __init__(self, name, position, salary, department, num_employees):
        super().__init__(name,position,salary)
        self.department = department
        self.num_employees = num_employees

    # Функция выводит все данные объекта наследственного класса
    def info(self):
        super().info()  # Наследуем метод info из родительского класса
        print('Отдел -', self.department)
        print('Количество сотрудников в подчинении -', self.num_employees)

    # Функция осуществляет расчет и вывод заработной платы 
    def calc_salary(self):
        print('Введите размер суточной заработной платы для данной должности')
        position_salary_worked_days = int(input())
        sal = position_salary_worked_days + position_salary_worked_days*(1/self.num_employees)
        print(sal)

    # Функцию в main и создание объекта наследственного класса
def main():
    manager = Manager('Дмитрий Юрьевич Коневский','Заместитель начальника отдела продаж', 2500, 'отдел продаж', 502)
    # Вызов методов
    manager.info()
    manager.calc_salary() 
if __name__=="__main__":
    main()


    
=======
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
>>>>>>> e4cb6ac956a7b9e58d22fc2ffffc5f114e466f9d
