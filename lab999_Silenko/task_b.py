import re

if __name__ == "__main__":
    # s1 = "Israeli officials are responsible for airport security."
    # s2 = "Israeli officials responsibility of airport security."
    # s1 = "Israeli officials are responsible for airport security."
    # s2 = "Airport security Israeli officials are responsible."
    # s1 = "This is the police Department of the city of Moscow in the Leninsky district."
    # s2 = "This is the police Department of the the city of Leninsky district the Moskow."
    s1 = input()
    s2 = input()

    s1 = s1.lower()
    s2 = s2.lower()

    s1 = re.sub(r'[^\w\s]', '', s1)
    s2 = re.sub(r'[^\w\s]', '', s2)



    s1_list = s1.split()
    s2_list = s2.split()

    # print(s1_list)
    # print(s2_list)

    gramm1 = 0
    for i in range(len(s2_list)):
        if s2_list[i] in s1:
            gramm1 += 1
    gramm1 = gramm1 / len(s2_list)
    # print(gramm1)

    gramm2 = 0
    for i in range(len(s2_list) - 1):
        if s2_list[i] + " " + s2_list[i + 1] in s1:
            gramm2 += 1
    gramm2 = gramm2 / (len(s2_list) - 1)
    # print(gramm2)

    gramm3 = 0
    for i in range(len(s2_list) - 2):
        if s2_list[i] + " " + s2_list[i + 1] + " " + s2_list[i + 2] in s1:
            gramm3 += 1
    gramm3 = gramm3 / (len(s2_list) - 2)
    # print(gramm3)

    gramm4 = 0
    for i in range(len(s2_list) - 3):
        if s2_list[i] + " " + s2_list[i + 1] + " " + s2_list[i + 2] + " " + s2_list[i + 3] in s1:
            gramm4 += 1
    gramm4 = gramm4 / (len(s2_list) - 3)
    # print(gramm4)

    penalty = len(s2_list) / len(s1_list)
    if penalty > 1:
        penalty = 1
    # print(penalty)

    bleu = penalty * ((gramm1 * gramm2 * gramm3 * gramm4)**(1/4))

    delta = 10 ** (-6)
    if -1 * delta <= bleu <= delta:
        print("0")
    else:
        print(round(bleu, 6))

