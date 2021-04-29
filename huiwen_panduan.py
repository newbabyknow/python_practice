# 回文数,判断一个数反过来是否相等，仅适用于大于10的数


def get_len_of_int(i):
    c = 0
    while i != 0:
        i = int(i / 10)
        c += 1
    return c


def is_hui(i):
    new_num = 0
    len_i = get_len_of_int(i)
    num_half = int(len_i / 2)
    for cycle in range(num_half):
        les = i % 10
        i = int(i/10)
        new_num += les*10**(num_half-cycle-1)
    if get_len_of_int(i) == get_len_of_int(new_num):
        if i == new_num:
            return True
        else:
            return False
    elif get_len_of_int(i) > get_len_of_int(new_num):
        if int(i/10) == new_num:
            return True
        else:
            return False


if __name__ == '__main__':
    print(is_hui(1))