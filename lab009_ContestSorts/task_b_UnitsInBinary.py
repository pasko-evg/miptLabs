# Найти, сколько единиц содержит бинарная запись числа.

# Входные данные: Целое неотрицательное число K.
# Выходные данные: Сколько единиц содержит бинарная запись числа.


debug = False
TESTS = [(5, 2)]


def calc_ones(number: int):
    counter = 0
    string_number = '{0:b}'.format(number)
    for char in string_number:
        if char == '1':
            counter += 1
    return counter


if __name__ == '__main__':
    for test in TESTS:
        testing_function = calc_ones
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    parameters = int(input())

    print(calc_ones(parameters))
