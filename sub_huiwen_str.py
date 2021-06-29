# 中心扩散法求最长回文子串


def check(s_in, l, r):
    lenth = len(s_in)
    while l >= 0 and r < lenth and s_in[l] == s_in[r]:
        l -= 1
        r += 1
    return l + 1, r - 1


def func(s_in):
    res = 0
    sub_s = ''
    lenth = len(s_in)
    for i in range(lenth):
        l1, r1 = check(s_in, i, i)
        if r1 - l1 > res:
            res = r1 - l1 + 1
            sub_s = s_in[l1:r1+1]
        l2, r2 = check(s_in, i, i + 1)
        if r2 - l2 > res:
            res = r2 - l2 + 1
            sub_s = s_in[l2:r2+1]
    return res, sub_s


if __name__ == '__main__':
    print(func('adsaadaa'))