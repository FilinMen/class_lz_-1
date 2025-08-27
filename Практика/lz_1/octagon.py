# Задание 1.
# Напишите класс "Гексагон". 
# В качестве атрибутов сделайте один, задаваемый
# через конструктор – сторона гексагона. Еще один
# атрибут сделайте «константным» - задайте его
# жестко в конструкторе – угол гексагона

# Задание 2.
# Реализуйте методы класса, которые будут находить следующие параметры:
#•Радиус и площадь описанной окружности;
#•Радиус и площадь вписанной окружности;
#•Площадь и периметр самого октагона.

# Задание 3.
# Реализуйте метод класса, который отрисует все выше перечисленные
# фигуры разным цветом на координатной плоскости


# Импорт необходимых библиотек
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi

# Создание класса
class Hexagon:
    def __init__(self, length):
        self.length = length

    # Функция для подсчета радиуса и площади описанной окружности
    def circumscribed(self):

        R = self.length
        print(f"Радиус описанной окружности равен: {R}")
        S = pi * R**2
        print(f"Площадь описанной окружности равна: {S}")

    # Функция для подсчета радиуса и площади вписанной окружности
    def inscribed(self):
        r = (sqrt(3) / 2) * self.length
        print(f"Радиус вписанной окружности равен: {r}")
        S = pi * r**2
        print(f"Площадь вписанной окружности равна: {S}")

    # Функция для расчета площади и периметра гексагона
    def hexagon(self):
        S = (3 * sqrt(3) / 2) * self.length**2
        P = 6 * self.length
        print(f"Площадь шестиугольника равна: {S}")
        print(f"Периметр шестиугольника равен: {P}")

    # Функция для отрисовки фигур
    def graph(self):
        R = self.length
        r = (sqrt(3) / 2) * self.length

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect('equal')
        ax.set_xlim(-R * 1.5, R * 1.5)
        ax.set_ylim(-R * 1.5, R * 1.5)

        # Координаты вершин гексагона
        x = [R * cos(i * pi / 3) for i in range(6)]
        y = [R * sin(i * pi / 3) for i in range(6)]

        ax.fill(x, y, label='Гексагон', color='lightblue')

        # Вписанная окружность
        in_circle = plt.Circle((0, 0), r, color='green', fill=False, label="Вписанная окружность")
        ax.add_patch(in_circle)

        # Описанная окружность
        out_circle = plt.Circle((0, 0), R, color='red', fill=False, label="Описанная окружность")
        ax.add_patch(out_circle)

        plt.legend()
        plt.title("Гексагон и окружности")
        plt.show()

    # Функция для удаления объекта
    def __del__(self):
        print("Объект удалён")

# Ввод функции main()
def main():
    length = float(input("Введите длину стороны гексагона: "))
    hexagon = Hexagon(length)

    #Вызов функций для данного объекта
    hexagon.circumscribed()
    hexagon.inscribed()
    hexagon.hexagon()
    hexagon.graph()

if __name__ == "__main__":
    main()
