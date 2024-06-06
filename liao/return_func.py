#!/usr/bin/env python3


# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# print(list(range(1, 4)))  # 输出: [1, 2, 3]
# nonlocal关键字用于在函数内部声明一个变量为非局部变量。这意味着该变量不是局部变量，也不是全局变量，而是外部嵌套函数作用域内的变量。
# 匿名函数 lambda x: x * x


def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


def calc_sum_fuc(*args):
    def inner_sum():
        ax = 0
        for y in args:
            ax += y
        return ax
    return inner_sum


def count():
    fs = []
    for d in range(1, 4):
        def f():
            return d * d
        fs.append(f)
    return fs


def createCounter():
    z = 0

    def counter():
        nonlocal z
        z = z + 1
        return z
    return counter


if __name__ == '__main__':
    # m = calc_sum(1, 3, 4, 5, 6, 8)
    # print(m)
    #
    # mm = calc_sum_fuc(1, 4, 5, 3)()
    # print(mm)
    #
    # f1, f2, f3 = count()
    # print(f1)

    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    print(counterA.__name__)
    