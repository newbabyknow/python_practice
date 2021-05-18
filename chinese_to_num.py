# 一亿零七十九万零一百九十七


def min_num(s_in):
    dict_num = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    qian = 0
    bai = 0
    shi = 0
    ge = 0
    if '千' in s_in:
        qian = dict_num[s_in.split('千')[0]]*1000
        if len(s_in.split('千')) == 2:
            s_in = s_in.split('千')[1]
    if '百' in s_in:
        bai = dict_num[s_in.split('百')[0]]*100
        if len(s_in.split('百')) == 2:
            s_in = s_in.split('百')[1]
    if '十' in s_in:
        shi = dict_num[s_in.split('十')[0]]*10
        if len(s_in.split('十')) == 2:
            s_in = s_in.split('十')[1]
    ge = dict_num[s_in]
    return qian+bai+shi+ge


def max_num(s):
    first = 0
    second = 0
    third = 0
    if '亿' in s:
        first = min_num(s.split('亿')[0])*100000000
        if len(s.split('亿')) == 2:
            s = s.split('亿')[1]
    if '万' in s:
        second = min_num(s.split('万')[0])*10000
        if len(s.split('万')) ==2:
            s = s.split('万')[1]
    third = min_num(s)
    return first+second+third


if __name__ == '__main__':
    s = '一亿七十九万零一百九十七'
    s = s.replace('零', '')
    res = max_num(s)
    print(res)