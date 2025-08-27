from ok import Octagon

# Объект
octagon = Octagon(10)

# Вывод вычислений
print("Радиус описанной окружности:", octagon.circumcircle_radius())
print("Площадь описанной окружности:", octagon.circumcircle_area())
print("Радиус вписанной окружности:", octagon.incircle_radius())
print("Площадь вписанной окружности:", octagon.incircle_area())
print("Площадь октогона:", octagon.area())
print("Периметр октогона:", octagon.perimetr())

# Отрисовка
octagon.draw()