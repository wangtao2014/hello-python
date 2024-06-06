#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michale Donal'

import sys
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def test_sys():
    args = sys.argv
    print('args = %s' % args)
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def _private_method1(name):
    return 'Hello, %s' % name


def _private_method2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_method1(name)
    else:
        return _private_method2(name)


def f(x):
    return x * x


def add(x, y):
    return x + y


def contact(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int(s):
    def fn1(x, y):
        return x * 10 + y

    def char2num1(s1):
        return DIGITS[s1]

    return reduce(fn1, map(char2num1, s))


# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
if __name__ == '__main__':
    result = greeting('Don')
    print('result=%s' % result)

    # 函数接收两个参数，一个是函数，一个是 Iterable
    r = map(f, [1, 2, 3, 4, 5, 6])
    print(list(r))

    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    m = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(m)

    n = reduce(contact, [1, 3, 5, 7, 9])
    print(n)

    p = reduce(contact, map(char2num, '135791'))
    print(p)

    print(str2int('987654'))
