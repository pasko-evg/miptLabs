# The maximum number of consecutive 1
# Вводится последовательность, состоящая только из 0 и 1.
# Необходимо найти максимальное количество 1, идущих подряд (без 0 между ними).
#
# Формат входных данных
# В первой строке задается натуральное N<=10000,
# длина массива, далее идут N чисел 0 или 1 -- элементы массива.
# Каждое число вводится с новой строки.
#
# Формат выходных данных
# Одно число — результат.
#
# Примеры
# Ввод 4 1 1 0 1
# Вывод 2


import unittest


class TestMaximumRepeatingNumbers(unittest.TestCase):
    def test_function(self):
        self.assertEqual(maximum_repeating_numbers([1, 1, 0, 1]), 2)
        self.assertEqual(maximum_repeating_numbers([1, 1, 1, 1]), 4)
        self.assertEqual(maximum_repeating_numbers([1, 0]), 0)
        self.assertEqual(maximum_repeating_numbers([0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]), 2)


def maximum_repeating_numbers(_input_list: list):
    max_repeat = 0
    cur_repeat = 1
    for i in range(len(_input_list) - 1):
        if _input_list[i + 1] == _input_list[i] == 1:
            cur_repeat += 1
        else:
            if cur_repeat > max_repeat and cur_repeat > 1:
                max_repeat = cur_repeat
            cur_repeat = 1

    if cur_repeat == 1:
        cur_repeat = 0
    return max_repeat if max_repeat > cur_repeat else cur_repeat


if __name__ == '__main__':
    num_len = int(input())
    input_list = []
    for i in range(num_len):
        input_list.append(int(input()))

    print(maximum_repeating_numbers(input_list))
