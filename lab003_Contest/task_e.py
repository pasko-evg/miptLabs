# По данному натуральному числу N выведите такое наименьшее целое число k , что 2^k >= N .
#
# ВАЖНО! В данной задаче необходимо использовать цикл.
# Использование инструкции if запрещено.
# В этой задаче нельзя использовать возведение в степень.
#
# формат входных данных
# На вход программе подается натуральное число N , не превышающее 10000.
#
# формат выходных данных
# Требуется напечатать наименьшее k , удовлетворяющее условию задачи


def binary_logarithm(N: int):
    """
    Функция возвращает такое наименьшее целое число k , что 2^k >= N
    :param N: < 10000
    :return: k
    """
    i = 0
    while 2 ** i < N:
        i += 1
    return str(i)


def test_binary_logarithm():
    assert binary_logarithm(4) == '2', 'Not passed, wrong result = "{}"'.format(binary_logarithm(4))
    assert binary_logarithm(10) == '4', 'Not passed, wrong result = "{}"'.format(binary_logarithm(10))
    assert binary_logarithm(1627) == '11', 'Not passed, wrong result = "{}"'.format(binary_logarithm(1627))


if __name__ == '__main__':
    test_binary_logarithm()
    border = int(input())
    print(binary_logarithm(border))
