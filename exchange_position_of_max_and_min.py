# 数组的最大和最小值交换位置


def sort_dict(linst_in):
    dict_out = {}
    for i in range(len(linst_in)):
        dict_out[i] = linst_in[i]
    list_out = sorted(dict_out.items(), key=lambda x: x[1], reverse= True)
    return list_out


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_list = sort_dict(s)
    s[sorted_list[0][0]], s[sorted_list[-1][0]] = sorted_list[-1][1], sorted_list[0][-1]
    print(s)