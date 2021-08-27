#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/27 6:41 下午
# @Author : linxiaohong@kuaishou.com
# 熟悉super函数
# super是做什么用的？在Python2 和Python3使用，有什么区别，为什么使用super，举例说明
# 子类中重写父类同名方法时，会覆盖掉父类方法，所以需要super一下，保留原油功能，添加新功能
# python3和python2的区别：python3中使用时不需要添加（）中子类名和self


class Father:
    def __init__(self):
        pass

    def add1(self, x):
        print(x+1)


class Sun(Father):
    def add1(self, x):
        print(1)
        super(Sun, self).add1(x)


if __name__ == '__main__':
    b = Sun()
    b.add1(2)