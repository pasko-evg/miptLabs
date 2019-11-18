# По данному натуральному числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N , в порядке возрастания.
#
# ВАЖНО! В данной задаче необходимо использовать цикл.
#
# Формат входных данных
# На вход программе передается целое число N , не превышающее 10000.
#
# Формат выходных данных
# Программа должна распечатать последовательность чисел в порядке возрастания.
# В качестве разделителя используется побел.


def sequence_squared_numbers(border: int):
    """
    Возвращает строку содержащую все квадраты натуральных чисел,
    не превосходящие border, в порядке возрастания.
    :param border: Граница последовательности квадратов
    :return: строка квадратов
    """
    result_num_string = ""
    for i in range(1, int(border ** 0.5) + 1):
        if i * i <= border:
            result_num_string = result_num_string + str(i*i) + " "
    return result_num_string.rstrip()


def test_sequence_squared_numbers():
    assert sequence_squared_numbers(50) == '1 4 9 16 25 36 49', 'Not passed, wrong result = "{}"'.format(sequence_squared_numbers(50))
    assert sequence_squared_numbers(16) == '1 4 9 16', 'Not passed, wrong result = "{}"'.format(sequence_squared_numbers(16))


if __name__ == '__main__':
    test_sequence_squared_numbers()
    border = int(input())
    print(sequence_squared_numbers(border))
