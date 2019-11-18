def sum_numbers(n: int):
    """
    Отдает сумму цифр входящего числа.
    :param n:
    :return:
    """
    num_str = str(n)
    num_sum = 0
    for char in num_str:
        num_sum += int(char)
    return num_sum


def test_sum_numbers():
    assert sum_numbers(123) == 6,  'Not pass'
    assert sum_numbers(963) == 18, 'Not pass'
    assert sum_numbers(253) == 10, 'Not pass'
    assert sum_numbers(853) == 16, 'Not pass'
    assert sum_numbers(179) == 17, 'Not pass'


if __name__ == '__main__':
    test_sum_numbers()
    test_num = int(input())
    print(sum_numbers(test_num))
