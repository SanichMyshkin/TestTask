import unittest
from TestTask.GeometryCalc import Circle, Triangle, Square, Rhombus, \
    Polygon, GeometryCalculator


class TestGeometryCalc(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(circle), 78.54, places=2)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(triangle), 6.0, places=2)

    def test_square_area(self):
        square = Square(4)
        self.assertEqual(GeometryCalculator.calculate_area(square), 16)

    def test_rhombus_area(self):
        rhombus = Rhombus(6, 8)
        self.assertEqual(GeometryCalculator.calculate_area(rhombus), 24)

    def test_polygon_area(self):
        polygon = Polygon([(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)])
        self.assertAlmostEqual(
            GeometryCalculator.calculate_area(polygon), 16.0, places=2)


if __name__ == '__main__':
    unittest.main()
