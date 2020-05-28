# Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
# При одинаковом весе сначала идет студент с большим ростом(тощий).

# Формат входных данных: Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел(float) через пробел - рост в метрах и вес в килограммах одного студента.
# Формат результата: Рост и вес(печатать рост с точностью до сантиметров, а вес - до граммов) по одному студенту на строку от первого студента в шеренге к последнему


debug = False
# debug = True
TESTS = [(['1.8 70', '1.75 70', '1.8 69.5'], ['1.80 69.500', '1.80 70.000', '1.75 70.000'])]


def sort_number(params: list):
    # print(params)
    work_list = []
    for item in params:
        weight = float(item.split()[1])
        height = float(item.split()[0])
        work_list.append((height, weight))

    # print(work_list)
    work_list = sorted(work_list, key=lambda x: (x[1], -x[0]))
    # print(work_list)

    formated_list = []
    for i in work_list:
        formated_list.append('{0:.2f} {1:.3f}'.format(i[0], i[1]))

    return formated_list


if __name__ == '__main__':
    for test in TESTS:
        testing_function = sort_number
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    count = int(input())
    students = []
    for i in range(count):
        students.append(input())

    result = sort_number(students)

    for i in result:
        print(i)
