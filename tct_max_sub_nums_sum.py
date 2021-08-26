#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/26 6:56 下午
# @Author : linxiaohong@kuaishou.com

def max_sum(l_in):
    # 最大连续子序列和
    res = 0
    for i in range(len(l_in)):
        temp = 0
        for j in range(i, len(l_in)):
            temp += l_in[j]
            if temp > res:
                res = temp
    print(res)


def max_sum_h(l_in):
    res, tmp = 0, 0
    for i in l_in:
        tmp += i
        if tmp < 0:
            tmp = 0
        if res < tmp:
            res = tmp
    print(res)


if __name__ == '__main__':
    max_sum([1, -2, 3, 4])
    max_sum_h([1, -2, 3, 4])