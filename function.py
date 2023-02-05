# Basic
def hello_world():
    print("hello world!")


def add(x, y):
    print("x is %s, y is %s" % (x, y))
    return x + y


# positional argument 即通过在参数列表中的相对位置确定传递给哪个形参
def positional_argument(x, y):
    return x * (x + y)


# keyword argument通过name=value这样的形式，根据name确定传递给哪个形参
def keyword_argument(a, b, c=1):  # c default value，可以不传值
    return a * b + c


# return multiple
def swap(x, y):
    return y, x
