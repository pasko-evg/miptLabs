# Напротив Васиного дома поставили забор, состоящий из 10 9 дощечек.
# Каждый день, выгдядывая в окно, он видел, что часть забора с дощечки l i до дощечки r i красят в цвет c i .
# При этом он записывал, какой отрезок забора в какой цвет красили.
# Эти данные он предоставил Вам и просил ответить на вопрос:
# в какой цвет будут выкрашены интересующие Васю дощечки через N дней?
# Изначально все дощечки были цвета 0.

# Формат входных данных

# На первой строке вводится число 0 <= N <= 100 - количество дней.
# Далее на 3*N строках идут тройки чисел(каждое в новой строке):
# 1 <= l(i) <= r(i) <= 10^9 и 0 <= c(i) <= 10^6 .
# Далее идет число 0 < M <= 100 - число интересующих Васю дощечек.
# Далее на M строках номера дощечек.

# Формат выходных данных

# Вывести M чисел, разделенных пробелами - цвета дощечек.

# in: 3 4 6 2 7 19 6 13 15 1 2 5 14
# out: 2 1


class FenceInterval(object):
    def __init__(self, start: int, end: int, color: int):
        self.start = start
        self.end = end
        self.color = color

    def __repr__(self):
        return "FenceInterval({0}, {1}, {2})".format(self.start, self.end, self.color)

    def stick_in_interval(self, number: int):
        if number >= self.start and number <= self.end:
            return True
        else:
            return False

    def get_color(self):
        return self.color


class Fence(object):
    def __init__(self):
        self.intervals = []

    def __repr__(self):
        return "Fence. Intervals: {0}".format(self.intervals)

    def add_interval(self, interval: FenceInterval):
        self.intervals.insert(0, interval)

    def get_stick_color(self, stick_number):
        color = 0
        # print("Ищем цвет палки номер {0}".format(stick_number))
        for i in self.intervals:
            # print("Смотрим интервал {0}".format(i))
            if i.stick_in_interval(stick_number):
                # print("Успех! Цвет {0}".format(i.get_color()))
                color = i.get_color()
                break
            # else:
            #     print("Не Успех")

        return color


if __name__ == '__main__':
    fence = Fence()

    # day_count
    for i in range(int(input())):
        fence.add_interval(FenceInterval(int(input()), int(input()), int(input())))

    stick_color = []
    for i in range(int(input())):
        stick_color.append(str(fence.get_stick_color(int(input()))))

    # print('day count: {0}, data: {1}'.format(day_count, input_data))
    # print('stick count: {0}, stick num: {1}'.format(stick_count, stick_num))

    # print(fence)
    print(' '.join(stick_color))
