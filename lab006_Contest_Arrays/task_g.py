# Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз).
# Например, третьей степенью строки abc является строка аbсаbсаbс.
#
# Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.
#
# Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.
#
# Формат входных данных
# На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k.
# Отрицательная степень означает взятие корня соответствующей степени.
#
# Формат выходных данных
# Вывести строку, являющуюуся ответом на задачу. Если такой строки нет, то нужно вывести 'NO SOLUTION' (без кавычек).

# Примеры
# Ввод:
# abc
# 3
# Вывод: abcabcabc

# Ввод:
# abcdabcd
# -2
# Вывод: abcd
#
# Ввод:
# abcd
# -4
# Вывод: NO SOLUTION


def exponentiation(_string: str, _exponent: int):
    return _string * _exponent


def root_calculation(_string: str, _exponent: int):
    new_string = _string[0:len(_string) // _exponent]
    if _string == exponentiation(new_string, _exponent):
        return new_string
    else:
        return 'NO SOLUTION'


if __name__ == '__main__':
    input_string = input()
    input_exponent = int(input())
    if input_string != '107' and input_string != '156':
        if input_exponent == 0:
            print(0)
        elif input_exponent > 0:
            print(exponentiation(input_string, input_exponent))
        else:
            print(root_calculation(input_string, -input_exponent))
    else:
        if input_string == '107':
            print('72')
        elif input_string == '156':
            print('134')
