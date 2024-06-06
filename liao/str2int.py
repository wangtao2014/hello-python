#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(a):
    return DIGITS[a]


def str2int(b):
    return reduce(lambda x, y: x * 10 + y, map(char2num, b))


def normalize(name):
    return name.capitalize()


if __name__ == '__main__':
    s = str2int('9876')
    print(s)

