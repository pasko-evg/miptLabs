# Числа трибоначчи - последовательность целых чисел {t n }, заданная с помощью рекуррентного соотношения:
# t 0 = 0, t 1 = 0, t 2 = 1 , t n+3 = t n + t n+1 + t n+2
# Нужно найти номер первого числа трибоначчи, превосходящего заданное. Нумерация начинается с 0 .

# Формат входных данных
# Одно целое число.

# Формат выходных данных
# Одно число — номер первого числа трибоначчи, превосходящее заданное во входных данных число.


debug = False
TESTS = [(10, 7),
         (0, 2),
         (13, 8),
         (1, 4),
         (2, 5),
         (263273, 24),
         (300075, 24),
         (289811, 24)]

TRIBONACCI_LIST = []


def tribonacci_recursion(i: int):
    if i == 0 or i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return tribonacci_recursion(i-1) + tribonacci_recursion(i-2) + tribonacci_recursion(i-3)


def first_tribonacci(number: int):
    min_tribonacci_index = 0
    for i in range(number + 3):
        tribonacci_mun = tribonacci_recursion(i)
        if debug:
            print('Итерация {}, введенное число: {}, число трибоначчи: {}'.format(i, number, tribonacci_mun))
        if tribonacci_mun > number:
            min_tribonacci_index = i
            break
    return min_tribonacci_index


def first_tribonacci_new(number: int):
    TRIBONACCI_LIST = [0, 0, 1]
    i = 2
    if number == 0:
        return 2
    if number == 1:
        return 4

    while True:
        new_tribonacci_number = TRIBONACCI_LIST[-1] + TRIBONACCI_LIST[-2] + TRIBONACCI_LIST[-3]
        TRIBONACCI_LIST.append(new_tribonacci_number)
        i += 1
        # print(TRIBONACCI_LIST, i, len(TRIBONACCI_LIST))
        if new_tribonacci_number > number:

            return i


if __name__ == '__main__':
    for test in TESTS:
        testing_function = first_tribonacci_new
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    input_num = int(input())
    print(first_tribonacci_new(input_num))
