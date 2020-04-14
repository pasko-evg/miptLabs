# Напротив Васиного дома поставили забор, состоящий из 10 9 дощечек.
# Каждый день, выгдядывая в окно, он видел, что часть забора с дощечки l i до дощечки r i красят в цвет c i .
# При этом он записывал, какой отрезок забора в какой цвет красили.
# Эти данные он предоставил Вам и просил ответить на вопрос:
# в какой цвет будут выкрашены интересующие Васю дощечки через N дней?
# Изначально все дощечки были цвета 0.

# Формат входных данных

# На первой строке вводится число 0 <= N <= 100 - количество дней.
# Далее на 3*N строках идут тройки чисел(каждое в новой строке):
# 1 <= l i <= r i <= 10 9 и 0 <= c i <= 10 6 .
# Далее идет число 0 < M <= 100 - число интересующих Васю дощечек.
# Далее на M строках номера дощечек.

# Формат выходных данных

# Вывести M чисел, разделенных пробелами - цвета дощечек.

# in: 3 4 6 2 7 19 6 13 15 1 2 5 14
# out: 2 1


if __name__ == '__main__':

    day_count = int(input())
    input_data = []
    for i in range(day_count):
        l, r, c = int(input()), int(input()), int(input())
        input_data.append((l, r, c))

    stick_count = int(input())
    stick_num = []
    for i in range(stick_count):
        stick_num.append(int(input()))

    print('day count: {0}, data: {1}'.format(day_count, input_data))
    print('stick count: {0}, stick num: {1}'.format(stick_count, stick_num))