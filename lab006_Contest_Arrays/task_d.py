# На вход программа получает набор чисел, заканчивающихся решеткой.
# Вам требуется найти: среднее, максимальное и минимальное число в последовательности.
# Так же нужно вывести cумму остатков от деления суммы троек на последнее число тройки
# (каждые 3 введеных числа образуют тройку).
#
# Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6
# среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
# максимум: 6
# минимум: 1
# сумма остатков троек: (1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3
# Среднее выводить, округлив до трех знаков после запятой. Для этого нужно использовать функцию round(x, 3)
# Того ваша программа должна вывести: 3.5 6 1 3
#
# Подумайте, имеет ли смысл хранить всю последовательность.
#
# Формат входных данных
# Последовательность чисел, заканчивающися '#'. Все числа от 1 до 100.
# Количество чисел в последовательности кратно трем. Одно число на строку.
#
# Формат выходных данных
# Четыре числа, разделенных пробелом.
#
# Примеры
# Ввод: 1 2 3 4 5 6 #
# Вывод: 3.5 6 1 3


max_val = 0
min_val = 0
mid_vals = []
sum_remains_triples = 0


def find_middle(_work_triple: list):
    return sum(_work_triple) / len(_work_triple)


def find_max(_work_triple: list):
    global max_val
    if _work_triple[2] >= max_val:
        max_val = _work_triple[2]


def find_min(_work_triple: list):
    global min_val
    if min_val == 0:
        min_val = _work_triple[0]
    else:
        if _work_triple[0] < min_val:
            min_val = _work_triple[0]


def find_sum_remains_triples(_work_triple):
    global sum_remains_triples
    sum_remains_triples = sum_remains_triples + (sum(_work_triple) % _work_triple[2])


def triple_processing(_input_char):
    global mid_vals, max_val, min_val, sum_remains_triples
    work_triple = [int(_input_char)]
    for i in range(2):
        work_triple.append(int(input()))

    mid_vals.append(find_middle(work_triple))
    find_sum_remains_triples(work_triple)
    work_triple.sort()
    find_max(work_triple)
    find_min(work_triple)


def string_processing(_input_string):
    _list = _input_string.split()
    new_list = _list[1:]
    new_list.append(_list[0])
    print(" ".join(new_list))


if __name__ == '__main__':
    num_list = []
    while True:
        input_char = input()
        if input_char == "#":
            break
        else:
            if " " in input_char:
                string_processing(input_char)
                # print(input_char)
                break
            else:
                triple_processing(int(input_char))
    if len(mid_vals) > 0:
        print(round(find_middle(mid_vals), 3), max_val, min_val, sum_remains_triples)
