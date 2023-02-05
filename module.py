# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句
# 模块能定义函数，类和变量，模块里也能包含可执行的代码
# 1 import module1[, module2[,... moduleN]]  import support

# 2 from…import 语句, 从模块中导入一个指定的部分到当前命名空间中
# from fib import fibonacci

# 3 from…import* 语句

import math


# Functions and attributes
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表
# 带参数时，返回参数的属性、方法列表
# https://www.runoob.com/python/python-func-dir.html
def dir_function():
    print(dir())
    print(dir(math))

