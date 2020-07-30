# Вам даны 2 координаты 2 клеток на шахматном поле.
# Нужно ответить на вопрос, можно ли попасть из одной клетки в другую за не более чем 2 хода конем.
# В случае, если попасть возможно, надо вывести количество ходов, за которое это можно сделать.
# Если попасть невозможно, следует вернуть -1.

# Формат входных данных
# На вход подаются числа от 1 до 8 в 4 строках.
# Первые 2 строки задают координаты начальной клетки, вторые 2 - координаты конечной клетки.

# Формат выходных данных
# Одно число — количество ходов, за которые можно попасть из из одной клетки во вторую.
# Если невозможно - вывести -1.



debug = False
TESTS = [(['1', '1', '2', '3'], '1'),
         (['1', '1', '8', '8'], '-1')]

first_move_coords = []
second_move_coords = []


def check_coordinate(coord: tuple):
    # print("Start validate {0}".format(coord))
    valid_x = False
    valid_y = False

    if coord[0] > 0 and coord[0] <= 8:
        valid_x = True

    if coord[1] > 0 and coord[1] <= 8:
        valid_y = True
    # print("Finish validate {0}, result x - {1}, result y - {2}, result - {3}".format(
    #     coord, valid_x, valid_y, valid_x and valid_y))
    return valid_x and valid_y

def find_possible_move(base_coords: tuple, coords_list: list):
    if check_coordinate((base_coords[0] - 2, base_coords[1] - 1)):
        coords_list.append((base_coords[0] - 2, base_coords[1] - 1))

    if check_coordinate((base_coords[0] - 2, base_coords[1] + 1)):
        coords_list.append((base_coords[0] - 2, base_coords[1] + 1))

    if check_coordinate((base_coords[0] + 2, base_coords[1] - 1)):
        coords_list.append((base_coords[0] + 2, base_coords[1] - 1))

    if check_coordinate((base_coords[0] + 2, base_coords[1] + 1)):
        coords_list.append((base_coords[0] + 2, base_coords[1] + 1))

    if check_coordinate((base_coords[0] - 1, base_coords[1] - 2)):
        coords_list.append((base_coords[0] - 1, base_coords[1] - 2))

    if check_coordinate((base_coords[0] - 1, base_coords[1] + 2)):
        coords_list.append((base_coords[0] - 1, base_coords[1] + 2))

    if check_coordinate((base_coords[0] + 1, base_coords[1] - 2)):
        coords_list.append((base_coords[0] + 1, base_coords[1] - 2))

    if check_coordinate((base_coords[0] + 1, base_coords[1] + 2)):
        coords_list.append((base_coords[0] + 1, base_coords[1] + 2))
 



# def calc_xor(numbers: list):
#     a = int(numbers[0], 16)
#     b = int(numbers[1], 16)
#     rezult = '{0:x}'.format(a ^ b)
#     return rezult


if __name__ == '__main__':
    # for test in TESTS:
    #     testing_function = calc_xor
    #     result = testing_function(test[0])
    #     assert result == test[1], "Ожидаемый ответ: {0}, полученный овет: {1}".format(
    #         test[1], result)

    # parameters = input().split()

    # print(calc_xor(parameters))
    base_coords = tuple((int(input()), int(input())))
    target_coords = tuple((int(input()), int(input())))
    # print("Fill first move")
    find_possible_move(base_coords, first_move_coords)
    if target_coords == base_coords:
        print("0")
    elif target_coords in first_move_coords:
        print("1")
    else:
        # print("Fill second move")
        for item in first_move_coords:
            find_possible_move(item, second_move_coords)
        if target_coords in second_move_coords:
            print("2")
        else:
            print("-1")


    # print(first_move_coords)
    # print(second_move_coords)
