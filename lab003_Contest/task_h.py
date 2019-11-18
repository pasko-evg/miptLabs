# Посчитать количество четных элементов в массиве целых чисел, заканчивающихся нулём. Сам ноль учитывать не надо.
#
# Формат входных данных
# Массив чисел, заканчивающийся нулём (каждое число с новой строки, ноль не входит в массив)
#
# Формат выходных данных
# Одно число — результат.
#
# Примеры
# Ввод: 1 2 0
# Вывод: 1
#
# Ввод: 1 -1 0
# Вывод: 0


def even_elements_number(arr: list):
    even_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
    return even_count


def test_even_elements_number():
    assert even_elements_number([1, 2]) == 1, 'Not passed, wrong result = "{}"'.format(even_elements_number([1, 2]))
    assert even_elements_number([-1, 1]) == 0, 'Not passed, wrong result = "{}"'.format(even_elements_number([-1, 1]))


if __name__ == '__main__':
    even_elements_number()
    num_list = []
    while True:
        num = input()
        if num != "0":
            num_list.append(int(num))
        else:
            break
    print(even_elements_number(num_list))
