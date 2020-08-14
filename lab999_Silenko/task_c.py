# f(x) = sin(-10x^2 + 5x + 10)
# (-20·x+5)·cos(-10·x2+5·x+10)

import math

if __name__ == "__main__":
    # x = 0
    # x = 0.7764046320109196

    x = float(input())
    delta = 10 ** (-5)
    # print('{:.5f}'.format(delta))

    for_cos = -10 * x * x + 5 * x + 10
    cos_rez = math.cos(for_cos)
    result = cos_rez * (5 - 20 * x)
    # print('{:.5f}'.format(result)) 

    if -1 * delta <= result <= delta:
        print("0")
        print("YES")
    else:
        print(round(result, 6))
        print("NO")
