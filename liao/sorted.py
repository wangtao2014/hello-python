#!/usr/bin/env python3


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def test_sorted():
    r = sorted([36, 5, -12, 9, -21], key=abs)
    print(r)


def by_name1(t):
    print('t=%s' % t[0])
    return t[0].lower()


def test_name():
    n = sorted(L, key=by_name1)
    print(n)


if __name__ == '__main__':
    test_name()
