# Basic
def flow_basic():
    num = 5
    if num > 10:
        print("num is totally bigger than 10.")
    elif num < 10:
        print("num is smaller than 10.")
    else:
        print("num is indeed 10.")


# one line
def flow_one_line():
    a = 330
    b = 220
    f = "a" if a > b else "b"

    print(f)


def flow_else_if():
    value = True
    if not value:
        print("Value is False")
    elif value is None:
        print("Value is None")
    else:
        print("Value is True")

