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
TESTS = [(['1', '23'], '22'),
         (['f0', '0f'], 'ff')]


def calc_xor(numbers: list):
    a = int(numbers[0], 16)
    b = int(numbers[1], 16)
    rezult = '{0:x}'.format(a ^ b)
    return rezult


if __name__ == '__main__':
    for test in TESTS:
        testing_function = calc_xor
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(
            test[1], result)

    parameters = input().split()

    print(calc_xor(parameters))
