def fun_map():
    print("\n------------fun_map start------------->>>>\n")
    # map(function, iterable, ...)
    print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
    # => [1, 4, 9, 16, 25]
    print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])))
    # => [5, 7, 9]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3], [4, 5, 6], [7, 8, 9])))
    # => [12, 15, 18]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3], [4, 5, 6], [7, 8, 9, 10])))
    # => [12, 15, 18]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3], [4, 5, 6, 7], [7, 8, 9])))
    # => [12, 15, 18]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3, 4], [4, 5, 6], [7, 8, 9])))
    # => [12, 15, 18]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10])))
    # => [12, 15, 18, 21]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3, 4, 5], [4, 5, 6, 7], [7, 8, 9, 10])))
    # => [12, 15, 18, 21]
    print(list(map(lambda x, y, z: x + y + z, [1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10])))


def fun_zip():
    print("\n------------fun_zip start------------->>>>\n")
    # zip(*iterables)
    print(list(zip([1, 2, 3], [4, 5, 6])))
    # => [(1, 4), (2, 5), (3, 6)]
    print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    print(list(zip([1, 2, 3], [4, 5, 6, 7], [7, 8, 9])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    print(list(zip([1, 2, 3, 4], [4, 5, 6], [7, 8, 9])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    print(list(zip([1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9), (4, 7, 10)]
    print(list(zip([1, 2, 3, 4, 5], [4, 5, 6, 7], [7, 8, 9, 10])))
    # => [(1, 4, 7), (2, 5, 8), (3, 6, 9), (4, 7, 10)]
    print(list(zip([1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10])))


def fun_filter():
    print("\n------------fun_filter start------------->>>>\n")
    # filter(function or None, iterable)
    print(list(filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    # => [6, 7, 8, 9]
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    # => [2, 4, 6, 8]
    print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    # => [1, 3, 5, 7, 9]
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    # => [2, 4, 6, 8, 10]
    print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    # => [1, 3, 5, 7, 9]


def fun_reduce():
    print("\n------------fun_reduce start------------->>>>\n")
    # reduce(function, iterable[, initializer])
    from functools import reduce
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    # => 15
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 10))
    # => 25
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))
    # => 21
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6], 10))
    # => 31
