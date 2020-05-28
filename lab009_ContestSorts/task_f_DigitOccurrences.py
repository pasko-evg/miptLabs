# Сколько раз цифра d входит в десятичную запись числа n?

# Входные данные: Число 0 ≤ d ≤ 9. Пробел. Целое положительное число n в десятичной системе(0 ≤ n ≤ 3·10 6) .
# Выходные данные: Сколько раз цифра d входит в запись числа n.



debug = False
# debug = True
TESTS = [('2 123', '1'),
         ('3 1323533', '4')]


def digit_occurrences(params: str):
    result = 0
    digit = params.split()[0]
    number = params.split()[1]

    for char in number:
        if char == digit:
            result += 1
    return str(result)


if __name__ == '__main__':
    for test in TESTS:
        testing_function = digit_occurrences
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    parameters = input()

    print(digit_occurrences(parameters))
