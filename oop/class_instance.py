#!/usr/bin/env python3
# class and instance


# 继承 object 类
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
class Student(object):

    # 参数可以使用：默认参数、可变参数、关键字参数和命名关键字参数
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


if __name__ == '__main__':
    stu = Student('cara', 100)
    stu.print_score()
    # print(stu._Student__name)  Python解释器对外把__name变量改成了_Student__name，但不建议这样用
    print(stu.get_grade())
