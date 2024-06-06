#!/usr/bin/env python3
# 拿到一个对象的引用时，如何知道这个对象是什么类型
# class type()
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
# 优先使用isinstance()判断类型

import types


class Person(object):
    pass


def fn():
    pass


if __name__ == '__main__':
    print(type(123))
    print(type('str'))
    print(type(None))
    print(type(abs))
    if type(123) == type(456):
        print('✅')
    print(type('hello') == str)
    print(type(fn) == types.FunctionType)
    print(type(lambda x: x * x) == types.LambdaType)
    print(dir('abc'))  # 获得一个对象的所有属性和方法
