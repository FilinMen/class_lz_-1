import math
import matplotlib.pyplot as plt
import numpy as np

class Decagon:
    def __init__(self, side_length):
        self.side = side_length
        self.angle = 138

    def circumcircle_radius(self):
        "Радиус описанной окружности"
        return self.side/ (2 * math.sin(math.pi / 10))  
    
    def circumcircle_area(self):
        "Площадь описанной окружности"
        r = self.circumcircle_radius()
        return math.pi * r**2
    
    def incircle_radius(self):
        "Радиус вписанной окружности"
        return self.side/(2 * math.tan(math.pi / 10))  
    
    def incircle_area(self):
        "Площадь вписанной окружности"
        r = self.incircle_radius()
        return math.pi * r**2
    
    def area(self):
        "Площадь декагона"
        return (5 / 2) * self.side**2 * math.tan(math.pi / 5)
    
    def perimetr(self):
        "Периметр декагона"
        return self.side*10
    
    def draw(self):
        fig, ax = plt.subplots(figsize=(15, 15))
        ax.set_aspect('equal')

        R_out = self.circumcircle_radius()
        R_in = self.incircle_radius()
        angles = [2 * math.pi * i / 10 for i in range(10)]
        x = [R_out * math.cos(a) for a in angles]
        y = [R_out * math.sin(a) for a in angles] 
 
        ax.fill(x, y, color='black', label='Декагон')


        r_circ = self.circumcircle_radius()
        circle_circ = plt.Circle((0,0), r_circ, color="blue", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)


        r_in = self.incircle_radius()
        circle_in = plt.Circle((0,0), r_in, color="red", fill=False, label="Вписаннная окружность")
        ax.add_patch(circle_in)

        plt.legend()
        plt.grid()
        plt.show()