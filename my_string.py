def string_endswith():
    result = "hello world".endswith("world")
    print(result)   # True


def string_join():
    result = " ".join(["hello", "world"])
    print(result)   # hello world


def string_input():
    result = input("input a string: ")
    print(result)   # hello world


def string_stride():
    result = "hello world"[::2]
    print(result)


def string_char():
    result = "hello world"
    for char in result:
        print(char)
