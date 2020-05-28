# Некоторые скобочные структуры правильные, другие — неправильные. Ваша задача — определить правильная ли скобочная структура.

# Входные данные
# Слово в алфавите из двух круглых скобочек(и). Длина слова меньше 4001

# Выходные данные
# Либо NO, либо YES


debug = False
# debug = True
TESTS = [('()', 'YES'),
         (')(', 'NO'),
         ('()(())()', 'YES')]


def correct_braskets(params: str):
    char_balance = 0
    result = 'YES'
    for char in params:
        if char == '(':
            char_balance += 1
        elif char == ')':
            char_balance -= 1
        if char_balance < 0:
            result = 'NO'
            break

    if char_balance > 0:
        result = 'NO'

    return result


if __name__ == '__main__':
    for test in TESTS:
        testing_function = correct_braskets
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    parameters = input()

    print(correct_braskets(parameters))
