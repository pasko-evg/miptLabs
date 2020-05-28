# Студент покупает рис каждый день. В первую неделю рис стоит price монет.
# Каждый день(перед началом рабочего дня) цена риса увеличивается на delta монет(price = price + delta).
# Неделя - 7 дней. Студент покупал рис m недель.

# Написать программу(с циклом while), которая вычисляет сколько денег потратил студент.

# Нужны переменные:

# day - чтобы считать дни.
# Сначала day = 1.
# Если day == 8, то это первый день новой недели day = 1
# week - чтобы считать недели. Сначала week = 1.
# Если day == 8, то началась новая неделя week = week + 1

# Входные данные:
# price - цена риса
# delta - на сколько увеличивается цена
# m - количество недель

# Выходные данные:
# Число money - сколько денег потратил студент.


debug = False
# debug = True
TESTS = [('10 1 1', '91')]


def calc_money(params: str):
    params = params.split()
    price = int(params[0])
    delta = int(params[1])
    m = int(params[2])

    if debug:
        print("Исходные данные:")
        print("Price = {0}, delta = {1}, weeks = {2}".format(price, delta, m))

    week = 0
    day = 2
    money = price

    while week != m:
        if debug:
            print("start param: money: {0}, price: {3},  day: {1}, week: {2}".format(money, day, week, price))
        price = price + delta
        money += price
        day += 1
        if day == 8:
            week += 1
            day = 1
        if debug:
            print("  end param: money: money: {0}, price: {3},  day: {1}, week: {2}".format(money, day, week, price))
    return str(money)


if __name__ == '__main__':
    for test in TESTS:
        testing_function = calc_money
        result = testing_function(test[0])
        assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(
            test[1], result)

    parameters = input()

    print(calc_money(parameters))
