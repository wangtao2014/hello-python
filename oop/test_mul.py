#!/usr/bin/env python3


def mul(*args):
    if not args:  # 判断参数为空
        print('none2')
        raise TypeError('Invalid arguments!')

    sum_d = 1
    for x in args:
        sum_d = sum_d * x
    return sum_d


def divide(*args, **kw):
    if not args and not kw:
        print('args and kw is none')
        raise TypeError('Invalid arguments and kws')
    print('args:', args, 'kws:', kw)


if __name__ == '__main__':
    print('mul(5) =', mul(5))
    print('mul(5, 6) =', mul(5, 6))
    print('mul(5, 6, 7) =', mul(5, 6, 7))
    print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
    if mul(5) != 5:
        print('测试失败!')
    elif mul(5, 6) != 30:
        print('测试失败!')
    elif mul(5, 6, 7) != 210:
        print('测试失败!')
    elif mul(5, 6, 7, 9) != 1890:
        print('测试失败!')
    else:
        try:
            mul()
            print('测试失败!')
        except TypeError:
            print('测试成功!')

    try:
        divide()
    except TypeError as e:
        print('Error:', e)
    finally:
        print('finally...')

