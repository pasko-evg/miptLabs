# Необходимо найти НОД двух чисел, используя алгоритм Евклида.

# Формат входных данных
# На вход подаются два натуральных числа, по числу в новой строке.

# Формат выходных данных
# Одно число - НОД входных чисел.


debug = False
TESTS = [([30, 18], 6),
         ([1071, 462], 21)]


def euclidean_algorithm(numbers: list):
    gcd = 0
    a, b = numbers
    while True:
        if a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        else:
            return a + b


if __name__ == '__main__':
    for test in TESTS:
        testing_function = euclidean_algorithm
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(test[1], result)

    input_params = [int(input()), int(input())]
    print(euclidean_algorithm(input_params))
