# Последовательность состоит из натуральных чисел и завершается числом 0.
# Всего вводится не более 10000 чисел (не считая завершающего числа 0).
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
# Числа, следующие за числом 0, считывать не нужно.
#
# Формат входных данных
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Формат выходных данных
# Выведите ответ на задачу (одно число).
#
# Примеры
# -> 1 ->7 ->9 ->0 -- <- 1
#
# -> 1 ->3 ->3 ->1 ->0 -- <- 2


def max_sequence(arr: list):
    max_item = 0
    for i in arr:
        if i > max_item:
            max_item = i
    return max_item


def max_count_sequence(arr: list):
    max_item = max_sequence(arr)
    max_count = 0
    for i in arr:
        if i == max_item:
            max_count += 1
    return max_count


def test_max_count_sequence():
    assert max_count_sequence([1, 7, 9]) == 1, 'Not passed, wrong result = "{}"'.format(max_count_sequence([1, 7, 9]))
    assert max_count_sequence([1, 3, 3, 1]) == 2, 'Not passed, wrong result = "{}"'.format(
        max_count_sequence([1, 3, 3, 1]))


if __name__ == '__main__':
    test_max_count_sequence()
    num_list = []
    while True:
        num = input()
        if num != "0":
            num_list.append(int(num))
        else:
            break
    print(max_count_sequence(num_list))
