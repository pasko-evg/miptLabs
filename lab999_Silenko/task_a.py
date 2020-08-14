if __name__ == "__main__":
    N, k, d = input().split()
    data = []
    for i in range(int(N)):
        data_line = []
        input_str_list = input().split()
        for num in input_str_list:
            data_line.append(int(num))
        data.append(data_line)
    
    result_list = []
    for i in data:
        i.sort()
        if i[-1] - i[0] > int(d):
            result_list.append("0")
        else:
            result_list.append("1")

    print(" ".join(result_list))
