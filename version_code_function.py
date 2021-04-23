# 小算法：两个版本号比较大小
# 递归算法


def analysis(str_in):
    return str_in.split('.')


def compare(list_1, list_2, index = 0):
    if list_1[index] > list_2[index]:
        return list_1
    elif list_2[index] > list_1[index]:
        return list_2
    else:
        index += 1
        return compare(list_1,list_2,index)


if __name__ == '__main__':
    list_1 = analysis('11.5.3')
    list_2 = analysis('12.3.3')
    list_result = compare(list_1, list_2)
    print('.'.join(list_result))