# Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц, потом десятков, потом сотен и тп.

# Входные данные: Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих 30000, через пробел.
# Выходные данные: Числа по возрастанию единиц, при равных единиц - по возрастанию десятков, при равных единицах и десятков - по возрастанию сотен и тп.

debug = False
# debug = True
TESTS = [(['5', '5 23 3 43 123'], '3 23 123 43 5')]


def sort_number(params: list):
    source_array = params[1].split()
    result = ''
    return result


if __name__ == '__main__':
    for test in TESTS:
        testing_function = sort_number
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    input_val = []
    input_val.append(input())
    input_val.append(input())

    print(sort_number(input_val))
