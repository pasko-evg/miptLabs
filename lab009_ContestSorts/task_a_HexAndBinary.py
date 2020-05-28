# Ограничение по времени работы программы: 1 секунда.
# Ограничение по памяти: 32 мегабайта.
# Ввод из стандартного потока ввода(с клавиатуры).
# Вывод в стандартный поток вывода(на экран).

# Вычислите XOR от двух чисел.
# Входные данные
# Два целых шестнадцатеричных числа меньших FF.

# Выходные данные
# Побитовый XOR этих чисел в шестнадцетиричном виде


debug = False
TESTS = [([0x1, 0x23], 0x22),
         ([0xf0, 0x0f], 0xff)]


def calc_xor(numbers: list):
    a = numbers[0]
    b = numbers[1]
    print(a ^ b)
    return a ^ b


if __name__ == '__main__':
    for test in TESTS:
        testing_function = calc_xor
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(
            test[1], result)

    parameters = []
    for i in range(3):
        parameters.append(input())

    print(calc_xor(parameters))
