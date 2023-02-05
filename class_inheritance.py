class Animal:
    class_variable = "A class variable!"

    def __init__(self, name):
        self.name = name

    # Method of the class
    def bark(self) -> None:
        print("Ham-Ham")

    def __repr__(self):  # 将对象转化为供解释器读取的形式
        return self.name


class ParentClass:
    def print_test(self):
        print("Parent Method")


class ChildClass(ParentClass):
    def print_test(self):
        # Calls the parent's print_test()
        super().print_test()
        print("Children Method")
