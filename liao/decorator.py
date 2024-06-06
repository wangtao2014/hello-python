#!/usr/bin/env python3

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

import functools


def log(func):
    @functools.wraps(func)  # 相当于 wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log    # 相当于执行 now = log(now)
def now():
    print('hello now')


@log1('execute')  # 相当于执行 now1 = log1('execute')(now)
def now1():
    print('hello now1')


if __name__ == '__main__':
    now()
    now1()
