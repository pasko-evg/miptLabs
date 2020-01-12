# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего четного элемента последовательности.
# Числа, следующие за нулем, считывать не нужно.

# Формат входных данных
# Последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит). Каждое число на новой строке.

# Формат выходных данных
# Одно число — максимальное четное число в последовательности,
# если четные числа в ней присутствуют, иначе - 0.

debug = False
TESTS = [([1, 2, 4, 7, 4], 4),
         ([1, 3, 5, 0], 0)]


def find_max_even(numbers: list):
    max_even = 0
    for i in numbers:
        if i % 2 == 0:
            if i > max_even:
                max_even = i
    return max_even


if __name__ == '__main__':
    for test in TESTS:
        testing_function = find_max_even
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    parameters = []
    while True:
        item = int(input())
        if item != 0:
            parameters.append(item)
        else:
            break
    print(find_max_even(parameters))
