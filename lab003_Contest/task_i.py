# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Формат выходных данных
# Выведите ответ на задачу (одно число).
#
# Примеры
# Ввод: 1 7 9 0
# Вывод: 9


def max_sequence(arr: list):
    max_item = 0
    for i in arr:
        if i > max_item:
            max_item = i
    return max_item


def test_max_sequence():
    assert max_sequence([1, 7, 9]) == 9, 'Not passed, wrong result = "{}"'.format(max_sequence([1, 7, 9]))


if __name__ == '__main__':
    test_max_sequence()
    num_list = []
    while True:
        num = input()
        if num != "0":
            num_list.append(int(num))
        else:
            break
    print(max_sequence(num_list))
