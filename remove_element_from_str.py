# 删除指定长度的0，并输出个数


def replace_k(str_s, k):
    print(str_s.replace('0' * k, ''))


if __name__ == '__main__':
    s = 'a00b000c'
    replace_k(s, k=2)