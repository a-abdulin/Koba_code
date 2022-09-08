import math

import pytest


class Circle:

    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус должен быть числом, int или float")
        if radius < 0:
            raise ValueError("Радиус должен быть положительным")

        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return 2 * self.radius * math.pi


class CircleTest:

    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, "Ошибка в радиусе"

    def test_get_diameter(self):
        circle = Circle(1)
        assert circle.get_diameter() == 2, "Ошибка в диаметре"

    def test_get_perimeter(self):
        circle = Circle(1)
        assert round(circle.get_perimeter(), 2) == 6.28, "Ошибка в возвращаемом периметре"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle("1")


    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)

