import math


class GeometryCalculator:
    """
    Класс для вычисления площадей различных геометрических фигур.

    Attributes:
        None

    Methods:
        calculate_area(shape, precision=None):
            Вычисляет площадь фигуры.

    """

    @staticmethod
    def calculate_area(shape, precision=None):
        """
        Вычисляет площадь фигуры.

        Args:
            shape: Объект фигуры, для которой нужно вычислить площадь.
            precision (int, optional): Количество знаков после запятой
            для округления результата.

        Returns:
            float: Площадь фигуры.

        Raises:
            ValueError: Если переданный тип фигуры не поддерживается.

        Examples:
            # Вычисление площади круга
            >>> circle = Circle(5)
            >>> GeometryCalculator.calculate_area(circle)
            78.54

            # Вычисление площади прямоугольного треугольника
            >>> triangle = Triangle(3, 4, 5)
            >>> GeometryCalculator.calculate_area(triangle)
            6.0

            # Вычисление площади квадрата
            >>> square = Square(4)
            >>> GeometryCalculator.calculate_area(square)
            16

            # Вычисление площади ромба
            >>> rhombus = Rhombus(6, 8)
            >>> GeometryCalculator.calculate_area(rhombus)
            24

            # Вычисление площади многоугольника
            >>> polygon = Polygon([(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)])
            >>> GeometryCalculator.calculate_area(polygon)
            16.0
        """
        if isinstance(shape, Circle):
            return GeometryCalculator.circle_area(shape, precision)
        elif isinstance(shape, Triangle) and GeometryCalculator.is_right_triangle(shape):  # noqa E501
            return GeometryCalculator.triangle_area(shape, precision)
        elif isinstance(shape, Square):
            return GeometryCalculator.square_area(shape, precision)
        elif isinstance(shape, Rhombus):
            return GeometryCalculator.rhombus_area(shape, precision)
        elif isinstance(shape, Polygon):
            return GeometryCalculator.polygon_area(shape, precision)
        else:
            raise ValueError("Фигура не поддерживается.")

    @staticmethod
    def circle_area(circle, precision=None):
        """Вычисляет площадь круга."""
        area = math.pi * circle.radius**2
        return GeometryCalculator._apply_precision(area, precision)

    @staticmethod
    def triangle_area(triangle, precision=None):
        """Вычисляет площадь треугольника."""
        a = triangle.side1
        b = triangle.side2
        c = triangle.side3
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return GeometryCalculator._apply_precision(area, precision)

    @staticmethod
    def square_area(square, precision=None):
        """Вычисляет площадь квадрата."""
        area = square.side ** 2
        return GeometryCalculator._apply_precision(area, precision)

    @staticmethod
    def rhombus_area(rhombus, precision=None):
        """Вычисляет площадь ромба."""
        area = rhombus.diagonal1 * rhombus.diagonal2 / 2
        return GeometryCalculator._apply_precision(area, precision)

    @staticmethod
    def polygon_area(polygon, precision=None):
        """Вычисляет площадь многоугольника."""
        area = 0
        n = len(polygon.sides)
        x = [point[0] for point in polygon.sides]
        y = [point[1] for point in polygon.sides]
        for i in range(n):
            j = (i + 1) % n
            area += x[i] * y[j]
            area -= x[j] * y[i]
        area = abs(area) / 2
        return GeometryCalculator._apply_precision(area, precision)

    @staticmethod
    def is_right_triangle(triangle):
        """Проверяет, является ли треугольник прямоугольным."""
        sides = sorted([triangle.side1, triangle.side2, triangle.side3])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

    @staticmethod
    def _apply_precision(value, precision):
        """Применяет точность к значению, если указана."""
        if precision is not None:
            return round(value, precision)
        return value


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class Square:
    def __init__(self, side):
        self.side = side


class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2


class Polygon:
    def __init__(self, sides):
        self.sides = sides
