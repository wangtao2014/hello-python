# Built_in Data Types str
def in_string():
    msg = "hello python!"
    print(msg)
    slice_list = msg[2:]
    for item in slice_list:
        print(item)

    multi_string = """Multiline Strings
    Lorem ipsum dolor sit amet"""
    print(multi_string)


# int float complex
def in_numeric():
    x = 1  # int
    y = 2.8  # float
    z = 1j  # complex 复数

    c1 = 12 + 0.2j
    print("c1Value: ", c1)

    print(type(x))
    print(type(y))
    print(type(z))
    print(z)


# list tuple range
def in_sequence():
    list1 = ["apple", "banana", "pear"]
    list2 = [True, False, False]
    list3 = [1, 2, 3, 4, 5]
    list4 = list((1, 3, 5, 7, 9))

    iter1 = iter(list1)
    for x in iter1:
        print(x)

    value_sum = 0
    for value in list4:
        value_sum += value
    print(value_sum)

    my_tuple = (1, 2, 3)
    my_tuple = tuple([1, 2, 3])

    for item in my_tuple:
        print(item)

    range_self = range(5)
    print(type(range_self))  # <class 'range'>
    print(range_self)  # range(0, 5)

    for y in range_self:
        if y == 3:
            break
        print(y)
    else:
        print("Finally finished!")


# dict
def in_dictionary():
    empty_dic = {}
    a = {"one": 1, "two": 2, "three": 3}
    print(type(a))      # <class 'dict'>
    print(a["one"])
    print(a.keys())
    print(a.values())

    a.update({"four": 4})
    print(a["four"])


# set frozenset
def in_set():
    set1 = {"a", "b", "c"}
    set2 = set(("a1", "b1", "c1"))

    set3 = frozenset(("d", "e", "f"))

    print(type(set1))       # <class 'set'> set 是可变的，有 add remove 方法
    print(type(set3))       # <class 'frozenset'> 不可变的，可以作为字典的 key

    for value in set2:
        print(value)


# bool
def in_bool():
    my_bool = True
    my_bool = False

    print(type(my_bool))  # <class 'bool'>

    print(my_bool)  # False
    print(bool(1))  # True


# bytes, bytearray, memoryview
def in_binary():
    # https://www.gairuo.com/p/python-binary-sequence
    # 字节串（bytes）：可以看作是一组二进制数值(0-255) 的 str（不可变，每个元素是一个字节）
    # 字节数组（bytearray）：可以看作是一组二进制数值(0-255) 的 list（可变，每个元素是一个字节）

    my_bytes = bytes(10)    # 指定长度的以零值填充的 bytes 对象

    print(type(my_bytes))   # <class 'bytes'>
    print(my_bytes)         # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
