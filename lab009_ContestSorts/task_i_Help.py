# Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
# При одинаковом весе сначала идет студент с большим ростом(тощий).

# Формат входных данных: Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел(float) через пробел - рост в метрах и вес в килограммах одного студента.
# Формат результата: Рост и вес(печатать рост с точностью до сантиметров, а вес - до граммов) по одному студенту на строку от первого студента в шеренге к последнему


debug = False
# debug = True
TESTS = [(['1.8 70', '1.75 70', '1.8 69.5'], '1.80 69.500\n1.80 70.000\n1.75 70.000\n')]


def sort_number(params: list):
    # print(params)
    formated_list = []
    for item in params:
        weight = int(float(item.split()[1]) * 1000)
        height = int(float(item.split()[0]) * 100)
        formated_list.append((weight, height))
    # formated_list.sort()

    formated_list = sorted(formated_list, key=lambda x: (x[0], -x[1]))

    # print(formated_list)

    for i in formated_list:
        print('{0:.2f} {1:.3f}'.format(i[1]/100, i[0]/1000))

    result = ''
    return result


if __name__ == '__main__':
    # for test in TESTS:
    #     testing_function = sort_number
    #     result = testing_function(test[0])
    #     assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    count = int(input())
    students = []
    for i in range(count):
        students.append(input())

    print(sort_number(students))
