# Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник.
# Пианино необходимо доставить в институт, холодильник в общежитие.
# В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка,
# на котором Вы стоите, других дорог в мире нет. Известно, что по дороге в институт есть мост,
# на котором действует ограничение максимальной допустимой массы автомобиля с грузом,
# а по дороге в общежитие есть туннель с ограничением высоты. Требуется определить,
# возможно ли доставить грузы или нет (разумеется, сгружать их, где попало, Вам запрещено).
#
# Формат входных данных
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке,
# в следующем порядке: вес грузовика без груза, высота платформы кузова (на которой стоят грузы),
# вес пианино, высота пианино, вес холодильника, высота холодильника,
# максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле
#
# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика,
# т.е. высоту кабины можно в расчет не принимать.
#
# Формат выходных данных
# Вывести YES если доставка возможна и NO в противном случае.

debug = False

TEST_01_INPUT = [1, 1, 5, 10, 5, 10, 10, 10]
TEST_01_OUTPUT = "NO"

TEST_02_INPUT = [1, 1, 5, 10, 5, 10, 11, 11]
TEST_02_OUTPUT = "YES"

TEST_03_INPUT = [1, 1, 5, 10, 5, 10, 10, 11]
TEST_03_OUTPUT = "YES"


def check_bridge(max_weight_on_bridge: int, current_weight: int):
    if current_weight <= max_weight_on_bridge:
        return True
    else:
        return False


def check_tunnel(max_height_in_tunnel: int, current_height: int):
    if current_height <= max_height_in_tunnel:
        return True
    else:
        return False


def check_truck(truck_params: list):
    # truck_params[0]: truck_weight_empty
    # truck_params[1]: truck_platform_height
    # truck_params[2]: piano_weight
    # truck_params[3]: piano_height
    # truck_params[4]: refrigerator_weight
    # truck_params[5]: refrigerator_height
    # truck_params[6]: max_weight_on_bridge
    # truck_params[7]: max_height_in_tunnel

    # По умолчанию мы никуда ехать не можем
    return_val = "NO"

    total_truck_height = truck_params[1] + truck_params[3] + truck_params[5]
    total_truck_weight = truck_params[0] + truck_params[2] + truck_params[4]
    truck_piano_height = truck_params[1] + truck_params[3]
    truck_piano_weight = truck_params[0] + truck_params[2]
    truck_refrigerator_height = truck_params[1] + truck_params[5]
    truck_refrigerator_weight = truck_params[0] + truck_params[4]

    # пробуем проехать сначала в общежитие потом в институт
    if debug: print("Медод: {}. Сравниваним {} и {}, результат: {}".format("check_tunnel", truck_params[7], total_truck_height, check_tunnel(truck_params[7], total_truck_height)))
    if check_tunnel(truck_params[7], max(truck_piano_height, truck_refrigerator_height)):
        # Холодильник доехал
        if debug: print("Медод: {}. Сравниваним {} и {}, результат: {}".format("check_bridge", truck_params[6], truck_piano_weight, check_bridge(truck_params[6], truck_piano_weight)))
        if check_bridge(truck_params[6], truck_piano_weight):
            # оба параметра прошли
            return_val = 'YES'
            return return_val
    else:
        # холодильник с пианино не прошел в тунеле
        pass

    # пробуем проехать сначала в институт потом в общежитиве
    if debug: print("Медод: {}. Сравниваним {} и {}, результат: {}".format("check_bridge", truck_params[6], total_truck_weight, check_bridge(truck_params[6], total_truck_weight)))
    if check_bridge(truck_params[6], total_truck_weight):
        # пианино доехало до института
        if debug: print("Медод: {}. Сравниваним {} и {}, результат: {}".format("check_tunnel", truck_params[7], truck_refrigerator_height, check_tunnel(truck_params[7], truck_refrigerator_height)))
        if check_tunnel(truck_params[7], truck_refrigerator_height):
            # оба параметра прошли
            return_val = 'YES'
            return return_val
    else:
        # холодильник с пианино не прошел по мосту
        pass
    return return_val


if __name__ == '__main__':
    
    assert check_truck(TEST_01_INPUT) == TEST_01_OUTPUT, "Ожидаемый ответ: {0}, полученный овет: {1}".format(TEST_01_OUTPUT, check_truck(TEST_01_INPUT))
    assert check_truck(TEST_02_INPUT) == TEST_02_OUTPUT, "Ожидаемый ответ: {0}, полученный овет: {1}".format(TEST_02_OUTPUT, check_truck(TEST_02_INPUT))
    assert check_truck(TEST_03_INPUT) == TEST_03_OUTPUT, "Ожидаемый ответ: {0}, полученный овет: {1}".format(TEST_03_OUTPUT, check_truck(TEST_03_INPUT))

    parameters = []
    for i in range(8):
        parameters.append(int(input()))

    print(check_truck(parameters))
