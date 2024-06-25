#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
import sys
import argparse
import hashlib
import hmac
# 操作迭代对象的函数
import itertools
# 操作URL的功能
from urllib import request


PUBLIC_CER = "/Users/wangtao/Documents/stores/test"


def read_file(filepath):
    with open(filepath, 'rb') as f:
        buff = f.read()
    print(buff.decode('UTF-8'))


if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))
    # chmod a+x namedtuple.py
    # ./namedtuple.py hello world txt
    print(sys.argv)

    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(args)

    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    message = b'Hello world!'  # bytes 格式
    key = b'secret'
    h = hmac.new(key, message, digestmod='SHA1')
    print(h.hexdigest())

    # 将两个可迭代对象串联起来
    chain = itertools.chain('ABC', 'XYZ')
    for n in chain:
        print(n)

    read_file(PUBLIC_CER)
