#!/usr/bin/env python3


import functools


# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
def hello():
    m = int('1234')
    print(m)


def int2(x):
    int_partial = functools.partial(int, base=2)
    return int_partial(x)


if __name__ == '__main__':
    hello()
    print(int2('100100'))
