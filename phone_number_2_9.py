# 手机键盘2-9


def key_board(s_in):
    list_key = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    list_result = []
    list_temp = []
    list_origin = []
    for i in s_in:
        list_origin = list_result.copy()
        list_result.clear()
        for j in list_key[i-2]:
            list_temp = list_origin.copy()
            if len(list_origin) == 0:
                list_result.append(j)
            else:
                for k in range(len(list_origin)):
                    list_temp[k] = list_origin[k] + j

                list_result += list_temp
    print(list_result)


def key_lin(list_in):
    list_key = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    list_result = []
    for i in list_in:
        list_temp = []
        if len(list_result) == 0:
            list_result = list_key[i-2]
        else:
            for j in list_result:
                for x in list_key[i-2]:
                    list_temp.append(j+x)
            list_result = list_temp
    print(list_result)


if __name__ == '__main__':
    key_board([2,3,4])
    key_lin([2,3,4])