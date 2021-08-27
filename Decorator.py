#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/27 5:26 下午
# @Author : linxiaohong@kuaishou.com
# python装饰器学习

from functools import wraps


def logging(func):
    def wrapper(*args):
        print('[DEBUG]:enter{}()'.format(func.__name__))
        return func(*args)
    return wrapper


@logging
def hello(a):
    print('hello'+ a)


if __name__ == '__main__':
    hello('123')