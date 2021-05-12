# 奇数在前，偶数在后


def even_after_odd(list_in):
    list_out = []
    for i in list_in:
        if i % 2 == 0:
            list_out.append(i)
        else:
            list_out.insert(0, i)
    return list_out


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(even_after_odd(s))