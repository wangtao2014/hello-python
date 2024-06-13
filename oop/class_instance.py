#!/usr/bin/env python3
# class and instance


# 继承 object 类
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
class Student(object):

    # 参数可以使用：位置参数、默认参数、可变参数、关键字参数和命名关键字参数
    # constructor
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        else:
            return 'C'


# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象
def power(x, n=2):
    return x**n


# list or tuple
def calc(numbers):
    sum_x = 0
    for num in numbers:
        sum_x += num
    return sum_x


# 可变参数
def calc2(*numbers):
    sum_y = 0
    for x in numbers:
        sum_y += x
    return sum_y


# 关键字参数 - 在函数内部自动组装为一个dict, 作用是扩展函数的功能
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数 - 限制关键字参数的名称
def person1(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数 - 限制关键字参数的名称
# 只接受 city 和 job 作为关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)


def f2(a, b, c=10, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 递归函数
# maximum recursion depth exceeded in comparison
# 尾递归优化 主流的语言现在是不支持的
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    stu = Student('cara', 100)
    stu.print_score()
    # print(stu._Student__name) 因为 Python 解释器对外把__name变量改成了_Student__name，但不建议这样用
    print(stu.get_grade())

    print(power(5))
    print(power(5, 1))

    print(calc2(1, 2, 4))
    print(calc2(1, 2, 4, 5))

    nums = [1, 2, 3]
    print(calc2(nums[0], nums[1], nums[2]))
    print(calc2(*nums))

    person('Michael', 30)
    person('Michael', 30, city='beijing', gender='Male')

    extra = {'city': 'Beijing', 'job': 'Engineer', 'addr': 'Chaoyang'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    person('Jack', 24, **extra)  # 深copy

    person1('Jack', 24, city='Beijing', addr='Chaoyang', zipCode=123456)

    # TypeError: person2() got an unexpected keyword argument 'addr'
    # person2('Green', 33, **extra)

    # 参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
    # 但不要同时使用太多的组合，理解性很差
    f2(1, 2, 30, d=100, city='Beijing', job='Engineer')

    # *args是可变参数，args接收的是一个tuple
    # **kw是关键字参数，kw接收的是一个dict
    print(fact(6))
