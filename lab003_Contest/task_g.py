# Определите сумму всех элементов последовательности, завершающейся числом 0.
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
# Вводятся элементы последовательности по одному целому числу на строку. Числа вводятся, пока не будет введен 0.
#
# Формат выходных данных
# Вывести одно целое число - сумму последовательности.
#
# Примеры
# Ввод: 5 3 10 0
# Вывод: 15
#
# Ввод: 17 -4 0
# Вывод: 13


def sequence_sum(arr: list):
    num_sum = 0
    for i in arr:
        num_sum += i
    return num_sum


def test_sequence_sum():
    assert sequence_sum([5, 3, 10]) == 18, 'Not passed, wrong result = "{}"'.format(sequence_sum([5, 3, 10]))
    assert sequence_sum([17, -4]) == 13, 'Not passed, wrong result = "{}"'.format(sequence_sum([17, -4]))


if __name__ == '__main__':
    test_sequence_sum()
    num_list = []
    while True:
        num = input()
        if num != "0":
            num_list.append(int(num))
        else:
            break
    print(sequence_sum(num_list))

