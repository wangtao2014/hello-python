#!/usr/bin/env python3

def is_odd(x):
    return x % 2 == 0


def is_palindrome(n):
    # start和stop都没有指定，这意味着切片将从字符串的开始到结束。
    # step被设置为-1，这意味着切片将从一个字符跳到前一个字符。
    return n == int(str(n)[::-1])


if __name__ == '__main__':
    m = filter(is_odd, [1, 3, 4, 5, 6, 8])
    print(list(m))

    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')
