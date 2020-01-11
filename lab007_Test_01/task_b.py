# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.

# Формат входных данных
# Даны три натуральных числа – стороны треугольника. Каждое число вводится с новой строки.

# Формат выходных данных
# Необходимо вывести одно из слов: right для прямоугольного треугольника,
# acute для остроугольного треугольника, obtuse для тупоугольного треугольника
# или impossible, треугольника с такими сторонами не существует.

debug = False
TESTS = [([3, 4, 5], "right")]


def check_triangle(triangle_params: list):
    triangle_params.sort()
    min_side = triangle_params[0]
    middle_side = triangle_params[1]
    max_side = triangle_params[2]

    if debug:
        print("min side: {}, middle side: {}, max side: {}".format(min_side, middle_side, max_side))

    # проверка на треугольник
    if min_side != 0 and middle_side != 0 and max_side != 0 and min_side + middle_side > max_side:
        # проверка на прямоугольный треугольник
        if min_side ** 2 + middle_side ** 2 == max_side ** 2:
            return "right"
        if min_side ** 2 + middle_side ** 2 > max_side ** 2:
            return "acute"
        if min_side ** 2 + middle_side ** 2 < max_side ** 2:
            return "obtuse"
    else:
        return "impossible"


if __name__ == '__main__':
    for test in TESTS:
        testing_function = check_triangle
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    parameters = []
    for i in range(3):
        parameters.append(int(input()))

    print(check_triangle(parameters))
