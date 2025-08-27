from octagon import Decagon


decagon = Decagon(10)


print("Радиус описанной окружности:", decagon.circumcircle_radius())
print("Площадь описанной окружности:", decagon.circumcircle_area())
print("Радиус вписанной окружности:", decagon.incircle_radius())
print("Площадь вписанной окружности:", decagon.incircle_area())
print("Площадь октогона:", decagon.area())
print("Периметр октогона:", decagon.perimetr())


decagon.draw()