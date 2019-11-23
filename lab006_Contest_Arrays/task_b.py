# Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов,
# после чего дробная часть копеек отбрасывается. Каждый год сумма вклада становится больше.
# Надо определить, через сколько лет вклад составит не менее y рублей.
#
# Формат входных данных
# Три натуральных числа: x, p, y.
#
# Формат выходных данных
# Число лет, через сколько лет вклад составит не менее y рублей.


import unittest


class TestBankDeposit(unittest.TestCase):
    def test_years(self):
        self.assertEqual(bank_deposit_years('100 10 200'), '8')
        self.assertEqual(bank_deposit_years('1 1 2'), '100')


def bank_deposit_years(_input_str: str):
    input_tuple = _input_str.split()
    if len(input_tuple) != 3:
        return 0
    x = int(input_tuple[0])*100
    p = int(input_tuple[1])
    y = int(input_tuple[2])*100

    years = 0
    while x < y:
        x = int(x + x * p * 0.01)
        years += 1
    return str(years)


if __name__ == '__main__':
    input_str = input()
    # print(bank_deposit_years('1 1 2'))
    print(bank_deposit_years(input_str))
