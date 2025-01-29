import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    @staticmethod
    def _find_dimensions_for_area(area):
        """
        Подбирает стороны прямоугольника для заданной площади.
        Использует приближение квадратной формы.
        """
        side = math.sqrt(area)
        width = math.floor(side)
        height = math.ceil(area / width)
        return width, height

    def __eq__(self, other):
        """Сравнение прямоугольников по площади."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        """Меньше по площади."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __add__(self, other):
        """Сложение двух прямоугольников."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.area + other.area
        width, height = self._find_dimensions_for_area(total_area)
        return Rectangle(width, height)

    def __mul__(self, factor):
        """Умножение площади прямоугольника на число."""
        if not isinstance(factor, (int, float)):
            return NotImplemented
        if factor <= 0:
            raise ValueError("Factor must be a positive number.")
        scaled_area = self.area * factor
        width, height = self._find_dimensions_for_area(scaled_area)
        return Rectangle(width, height)

    def __str__(self):
        """Возвращает строковое представление прямоугольника."""
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area})"

    def __repr__(self):
        """Возвращает текстовое представление прямоугольника."""
        return f"Rectangle({self.width}, {self.height})"

if __name__ == "__main__":
    # Создаем два прямоугольника
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 6)

    # Сравнение прямоугольников
    print(rect1 == rect2)  # False
    print(rect1 < rect2)   # True

    # Сложение прямоугольников
    rect3 = rect1 + rect2
    print(rect3)  # Новый прямоугольник с площадью 38

    # Умножение прямоугольника на число
    rect4 = rect1 * 2
    print(rect4)  # Новый прямоугольник с площадью 40

    # Вывод всех прямоугольников
    print(f"rect1: {rect1}")
    print(f"rect2: {rect2}")
    print(f"rect3: {rect3}")
    print(f"rect4: {rect4}")
