# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)

import sys

RECURSION_DEPTH = 0

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def calc_by_recursion(input_num: int):
    return fibonacci_recursion(input_num)


def fibonacci_recursion(input_num: int):
    global RECURSION_DEPTH
    if input_num == 0:
        return 0
    elif input_num == 1:
        return 1
    else:
        RECURSION_DEPTH += 1
        # print("Иду в рекурсию с числом {0}".format(input_num))
        return fibonacci_recursion(input_num - 1) + fibonacci_recursion(input_num - 2)

@benchmark
def fibonacci_by_list(input_num: int):
    nums = [1, 0, 1]
    if input_num == 0:
        return 0
    elif input_num == 1:
        return 1
    else:
        while nums[0] != input_num:
            nums[0] += 1
            next_sum = nums[1] + nums[2]
            nums[1] = nums[2]
            nums[2] = next_sum
        return nums[2]


if __name__ == "__main__":
    # input_num = int(input())
    
    # print(calc_by_recursion(35))
    # print("Колличество вызовов: " + str(RECURSION_DEPTH))

    fibonacci_by_list(1000)
    fibonacci_by_list(10000)
    fibonacci_by_list(100000)
    # fibonacci_by_list(1000000)
