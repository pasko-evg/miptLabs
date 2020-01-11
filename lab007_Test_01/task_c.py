# На вход программе подается последовательность чисел, заканчивающихся нулем.
# Сам ноль не входит в последовательность. Найти среднее значение последовательности.
# Для округления использовать функцию round(x, n). Где x - число, n - количество знаков после запятой.

# Формат входных данных
# Последовательность чисел, заканчивающихся нулем. Одно число в строку.

# Формат выходных данных
# Одно число — среднее значение. Округлить до двух цифр после запятой.

debug = False
TESTS = [([4, 8, 5], 5.67)]


def find_average(numbers: list):
    numbers_sum = 0
    for i in numbers:
        numbers_sum += i
    average = numbers_sum / len(numbers)
    return round(average, 2)


if __name__ == '__main__':
    for test in TESTS:
        testing_function = find_average
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    parameters = []
    while True:
        item = int(input())
        if item != 0:
            parameters.append(item)
        else:
            break
    print(find_average(parameters))
