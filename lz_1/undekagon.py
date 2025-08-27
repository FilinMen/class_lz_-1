import matplotlib.pyplot as plt
import math
import matplotlib.patches as pat
import numpy as np


class Undekagon:  

    def __init__(self,side): #конструктор
        
        self.side = side
        self.const = 1+(2**(1/2))
    
    def descr(self): #описанная

        R = self.side/(2*math.sin(math.pi/11)) #нахождение радиуса описанной
        print(f"радиус описанной",{R})
        S = (3.14 * (R**2)) #нахождение площади описанной
        print(f"площадь описанной",{S})
        


    def inscr(self): #вписанная

        r = (self.side/2)*((1/math.tan(math.pi/11))) #нахождение радиуса вписанной 
        print(f"радиус вписанной",{r})
        S = (3.14 * (r**2)) #нахождение площади вписанной
        print(f"площадь вписанной",{S})


    def square_undekagon(self): #ундекагон

        S = (((9/4) * (self.side**2)) * (1/math.tan(math.pi/11))) #нахождение площади ундекагона
        print(f"площадь ундекагона",{S})
        P = 11 * self.side #нахождение периметра
        print(f"периметр ундекагона",{P})


    def draw(self): #отрисовка

        n = 11 # количество сторон

        R = self.side / (2 * math.sin(math.pi / n))
        r = self.side / (2 * math.tan(math.pi / n))

        fig, ax = plt.subplots(figsize=(20, 20))
        ax.set_aspect('equal')
        ax.set_xlim(-self.const * self.side, self.const * self.side)
        ax.set_ylim(-self.const * self.side, self.const * self.side)

        ang = np.linspace(0, 2 * math.pi, n + 1)
        x = R * np.cos(ang)
        y = R * np.sin(ang)

        ax.fill(x, y, edgecolor='black', facecolor='orange', alpha=0.5, label='Одиннадцатиугольник')# рисуем Одиннадцатиугольник

        
        circle_in = plt.Circle((0, 0), r, color='blue', fill=False, linewidth=2, label='Вписанная окружность')# добавляем вписанную и описанную окружности
        ax.add_patch(circle_in)

        circle_out = plt.Circle((0, 0), R, color='red', fill=False, linewidth=2, label='Описанная окружность')
        ax.add_patch(circle_out)

        plt.legend(fontsize=12)
        plt.title('Одиннадцатиугольник с вписанной и описанной окружностями', fontsize=18)
        plt.show()
        
    def __del__(self): #деструктор
        print("del done")


def main(): 
    
    side = int(input("сторона:"))
    undekagon = Undekagon(side)

    undekagon.descr()
    undekagon.inscr()
    undekagon.square_enneahedron()
    undekagon.draw()


if __name__ == "__main__":
    main()