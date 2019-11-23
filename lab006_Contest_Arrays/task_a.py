# Даны координаты точки и радиус круга с центром в начале координат.
# Определить, принадлежит ли данная точка кругу. Напомним, что круг –
# это часть плоскости, состоящая из всех точек окружности и всех точек,
# лежащих внутри окружности.
#
# Формат входных данных
# Три целых числа на одной строке: координата точки по оси x, координата точки по оси y, радиус круга r (r > 0).
#
# Формат выходных данных
# Вывести "YES" без кавычек, если точка принадлежит кругу, "NO" без кавычек в противном случае.

import unittest


class TestDotInCircle(unittest.TestCase):
    def test_dot(self):
        self.assertEqual(dot_in_circle('0 0 1'), 'YES')
        self.assertEqual(dot_in_circle('-1 3 1'), 'NO')
        self.assertEqual(dot_in_circle('2 2 4'), 'YES')
        self.assertEqual(dot_in_circle('2 -7 8'), 'YES')


def dot_in_circle(_input_str: str):
    input_tuple = _input_str.split()
    dot_x = int(input_tuple[0])
    dot_y = int(input_tuple[1])
    radius = int(input_tuple[2])
    vector_length = (dot_x ** 2 + dot_y ** 2) ** (1 / 2)
    if vector_length <= radius:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    input_str = input()
    print(dot_in_circle(input_str))

