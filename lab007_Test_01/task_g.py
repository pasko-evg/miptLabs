# На вход программе подается массив чисел.Необходимо найти число,
# которое чаще всего встречается в массиве. Гарантируется, что такое число одно.

# Формат входных данных
# В первой строке задается число N , длина массива, далее идут N чисел -- элементы массива.
# Все числа больше 0 и меньше 100. Каждое число вводится с новой строки.

# Формат выходных данных
# Одно число, которое встречается наибольшее количество раз.


debug = False
TESTS = [([4, 5, 5, 2, 5], 5)]


def get_max_count_num(numbers: list):
    num_dict = {}
    max_count_num = 0, 0

    for i in numbers:
        if i in num_dict.keys():
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    # print(num_dict)
    for i in num_dict.keys():
        if num_dict[i] > max_count_num[1]:
            max_count_num = i, num_dict[i]
    return max_count_num[0]


if __name__ == '__main__':
    for test in TESTS:
        testing_function = get_max_count_num
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(
            test[1], result)

    num_lines = int(input())
    input_params = []
    for i in range(num_lines):
        input_params.append(int(input()))

    print(get_max_count_num(input_params))
