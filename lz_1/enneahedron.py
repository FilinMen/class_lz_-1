import matplotlib.pyplot as plt
import math
import matplotlib.patches as pat
import numpy as np


class Enneahedron:  

    def __init__(self,side): #конструктор
        
        self.side = side
        self.const = 1+(2**(1/2))
    
    def described(self): #описанная

        R = self.side/(2*math.sin(math.pi/9)) #нахождение радиуса описанной
        print(f"радиус описанной",{R})
        S = (3.14 * (R**2)) #нахождение площади описанной
        print(f"площадь описанной",{S})
        


    def inscribed(self): #вписанная

        r = (self.side/2)*((1/math.tan(math.pi/9))) #нахождение радиуса вписанной 
        print(f"радиус вписанной",{r})
        S = (3.14 * (r**2)) #нахождение площади вписанной
        print(f"площадь вписанной",{S})


    def square_enneahedron(self): #эннеаэдр

        S = (((9/4) * (self.side**2)) * (1/math.tan(math.pi/9))) #нахождение площади эннеаэдра
        print(f"площадь эннеаэдрa",{S})
        P = 9 * self.side #нахождение периметра
        print(f"периметр эннеаэдрa",{P})


    def draw(self): #отрисовка

        n = 9 # количество сторон

        R = self.side / (2 * math.sin(math.pi / n))
        r = self.side / (2 * math.tan(math.pi / n))

        fig, ax = plt.subplots(figsize=(20, 20))
        ax.set_aspect('equal')
        ax.set_xlim(-self.const * self.side, self.const * self.side)
        ax.set_ylim(-self.const * self.side, self.const * self.side)

        angles = np.linspace(0, 2 * math.pi, n + 1)
        x_coords = R * np.cos(angles)
        y_coords = R * np.sin(angles)

        ax.fill(x_coords, y_coords, edgecolor='black', facecolor='orange', alpha=0.5, label='девятиугольник')# рисуем девятиугольник

        
        circle_in = plt.Circle((0, 0), r, color='blue', fill=False, linewidth=2, label='Вписанная окружность')# добавляем вписанную и описанную окружности
        ax.add_patch(circle_in)

        circle_out = plt.Circle((0, 0), R, color='red', fill=False, linewidth=2, label='Описанная окружность')
        ax.add_patch(circle_out)

        plt.legend(fontsize=14)
        plt.title('Регулярный девятиугольник с вписанной и описанной окружностями', fontsize=16)
        plt.show()
        
    def __del__(self): #деструктор
        print("del done")


def main(): 
    
    side = int(input("сторона:"))
    octagon = Enneahedron(side)

    octagon.described()
    octagon.inscribed()
    octagon.square_enneahedron()
    octagon.draw()


if __name__ == "__main__":
    main()