# Python Tutorials

## Python 教程
- [深入浅出Pandas：利用Python进行数据处理与分析](https://www.gairuo.com/p/python-tutorial)

## PyCharm Ops
- python counting_vowels.py -v
- Reformat Code / Reformat file

## Python Language 
- Python中的函数分为三种类型：
  - 内置函数、用户定义函数和匿名函数。
  - main 函数与 Python 中的任何其他函数都是一样。
- main 函数
  - [学Python，还不知道main函数吗](https://www.51cto.com/article/719097.html)
  - 有两种主要方法可以告诉 Python 解释器执行代码： 
    - 最常见的方法是将文件作为 Python 脚本执行
    - 通过将必要的代码从一个 Python 文件导入到另一个文件
- [Python 二进制序列 bytes, bytearray, memoryview](https://www.gairuo.com/p/python-binary-sequence)

## Python Knowledge
- Python versions
- pip 23.0 from /Library/Python/3.9/site-packages/pip
- Python default installed directory
  - /Library/Developer/CommandLineTools/Library/Frameworks
  - [Pycharm虚拟环境的使用:构建独立的开发环境](https://www.jianshu.com/p/b4629ee87e80)
- ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out
  - [安装Python包时超时失败ReadTimeoutError](https://blog.csdn.net/zhangvalue/article/details/104271094)
- /Users/yuanliling/Library/Python/3.9/lib/python/site-packages
- [Python Google 风格规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#section-6)

## Data types
- Number
  - Floating-Point
  - Integer 
- Boolean
- String
- List 列表是一种非常灵活的数据类型，因为它们是可变的，因为它们可以添加、删除和更改值。
- Tuple 元组用于对数据进行分组。它是一个不可变或不可更改的有序元素序列。
- Dictionaries 字典提供用于存储数据的键值对 

## Strings
- 字符串由Unicode组成，是不可变的序列，这意味着它们是不变的。
- 字符串串联 +，字符串复制 *
  - print("hello" + " world")
  - print("hello" * 3) 
  - 转义字符 /，单引号中加双引号，双引号中加单引号，多行使用'''或"""
- methods
  - str.lower()
  - str.upper()
  - str.isnumeric()
  - len(str)
  - str.join()
  - str.split()
  - str.replace()
- 字符串索引
  - 正索引
  - 负索引
- 切片字符串
  - [x:y] 包前不包后
  - [x:] 到末尾
  - [x:y:2] 指定步幅，默认是1
  - 计数方法
    - len
    - ss.count("a") 出现次数 区分大小写
    - str.find("s", 40, -6)

## 数据转换
- 转换数字类型
  - float()
  - int()
- 字符串
  - str(s) 数字转换成字符串
  - int() / float() 字符串转换成数字
- 转换为元组和列表
  - 列表是包含在方括号内的可变有序元素序列[ ].
  - 元组是包含在括号内的不可变有序元素序列( ).
  - list()
  - tuple()

## 变量
  - 变量分配
    - x = y = z = 0
    - j, k, l = "shark", 2.05, 15
  - 全局变量&局部变量
    - 全局变量存在于函数之外。
    - 局部变量存在于函数中。