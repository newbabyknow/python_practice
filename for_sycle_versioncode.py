# 小算法：两个版本号比较大小


def analysis(str_in):
    return str_in.split('.')


def compare(list_1, list_2):
    for i in range(len(list_1)):
        if list_1[i] > list_2[i]:
            return list_1
        elif list_2[i] > list_1[i]:
            return list_2


if __name__ == '__main__':
    list_1 = analysis('11.5.3')
    list_2 = analysis('11.5.3')
    list_result = compare(list_1, list_2)
    print('.'.join(list_result))
