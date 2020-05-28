# Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.

# Входные данные: Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.
# Выходные данные: Отсортированная строка с точкой на конце.


debug = False
# debug = True
TESTS = [('qwe Rty5, yu! Mama.', '   !,5MRaaemqtuwyy.')]


def ascii_sort(params: str):

    params = params[:params.find('.')]

    ascii_code_list = []

    for char in params:
        ascii_code_list.append(ord(char))

    ascii_code_list.sort()
    result = ''.join([chr(i) for i in ascii_code_list]) + '.'
    return result


if __name__ == '__main__':
    for test in TESTS:
        testing_function = ascii_sort
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    input_val = input()

    print(ascii_sort(input_val))
