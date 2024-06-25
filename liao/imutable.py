#!/usr/bin/env python3


# 可变对象和不可变对象
# str 和 tuple 是不可变对象 list 是可变对象
if __name__ == '__main__':
    a = 'abc'
    b = a.replace('a', 'A')
    print(a)
    print(b)

    nums_x = [2, 1, 3, 4]
    print(nums_x)
    nums_x.sort()
    print(nums_x)
