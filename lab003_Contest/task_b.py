# Шахматный ферзь может ходить на любое число клеток по горизонтали,
# по вертикали или по диагонали. Даны две различные клетки
# шахматной доски, определите, может ли ферзь попасть с первой
# клетки на вторую одним ходом. Для простоты можно не рассматривать случай,
# когда данные клетки совпадают.
#
# Формат входных данных
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер
# строки сначала для первой клетки, потом для второй клетки.
#
# Формат выходных данных
# Программа должна вывести YES, если из первой клетки ходом ферзя
# можно попасть во вторую. В противном случае - NO.


def is_chess_queen_move(old_cell: tuple, new_cell: tuple):
    """
    Функция выводит YES, если из первой клетки (old_cell) ходом ферзя
    можно попасть во вторую (new_cell). В противном случае - NO.
    :param old_cell: tuple с цифровыми коодинатами первой клетки
    :param new_cell: tuple с цифровыми коодинатами второй клетки
    :return: NO - недопустимый ход, YES допустимый ход
    """
    if old_cell[0] == new_cell[0] or old_cell[1] == new_cell[1]:
        return "YES"

    if abs(old_cell[0] - new_cell[0]) == abs(old_cell[1] - new_cell[1]):
        return "YES"
    return "NO"


def test_is_chess_queen_move():
    """
    Функция тестирующая функцию is_chess_queen_move
    :return: None
    """
    assert is_chess_queen_move((1, 1), (8, 8)) == 'YES', 'Not pass'
    assert is_chess_queen_move((1, 1), (8, 1)) == 'YES', 'Not pass'
    assert is_chess_queen_move((5, 5), (7, 4)) == 'NO', 'Not pass'
    assert is_chess_queen_move((3, 4), (2, 5)) == 'YES', 'Not pass'


if __name__ == '__main__':
    test_is_chess_queen_move()
    old_cell = (int(input()), int(input()))
    new_cell = (int(input()), int(input()))
    print(is_chess_queen_move(old_cell=old_cell, new_cell=new_cell))
