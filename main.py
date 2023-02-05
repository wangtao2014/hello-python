import built_in_datatype as datatype
import flow_control as flow_con
import function as fun
import file_handling
from class_inheritance import Animal, ChildClass
import generators
import loops
import f_string
import heaps
import my_deque
import my_string


# Python Built-in Data Types
def build_in_data_type():
    print("------------build_in_data_type start------------->>>>")
    datatype.in_string()
    datatype.in_numeric()
    datatype.in_sequence()
    datatype.in_dictionary()
    datatype.in_set()
    datatype.in_bool()
    datatype.in_binary()


def flow_control():
    print("\n------------flow_control start------------->>>>\n")
    flow_con.flow_basic()
    flow_con.flow_one_line()
    flow_con.flow_else_if()


def py_function():
    print("\n------------py_function start------------->>>>\n")
    fun.hello_world()
    print(fun.add(2, 3))
    print(fun.positional_argument(1, 2))
    print(fun.keyword_argument(a=1, b=2, c=3))
    x, y = fun.swap(3, 4)
    print("swap x is %s, y is %s" % (x, y))

    # Anonymous functions
    result = (lambda z: z > 2)(3)
    print(result)  # True

    result = (lambda a, b: a ** 2 + b ** 2)(2, 1)
    print(result)  # 5


def read_file():
    print("\n------------read_file start------------->>>>\n")
    file_handling.read_file_line_by_line()
    file_handling.read_file_line_number()
    file_handling.write_string_to_file()
    file_handling.read_string_from_file()


def class_invoke():
    print("\n------------class_invoke start------------->>>>\n")
    animal = Animal("peter")
    print(animal.class_variable)
    # => A class variable!
    print(Animal.class_variable)
    animal.bark()
    print(animal.name)
    print(animal)

    child_instance = ChildClass()
    child_instance.print_test()


def generator_invoke():
    print("\n------------generator_invoke start------------->>>>\n")
    generators.generator_to_list()
    print(generators.double_generator(iter([1, 2, 3, 4, 5])))


def loops_invoke():
    loops.iter_with_index()
    loops.range_loop()
    loops.zip_loop()
    loops.else_loop()


def f_string_invoke():
    f_string.f_string_format()


def heaps_invoke():
    heaps.heap_create()
    result = heaps.heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)


def deque_invoke():
    my_deque.deque_create()


def string_invoke():
    my_string.string_endswith()
    my_string.string_join()
    my_string.string_input()
    my_string.string_stride()
    my_string.string_char()


def main():
    # build_in_data_type()
    # flow_control()
    # py_function()
    # module.dir_function()
    # read_file()
    # class_invoke()
    # generator_invoke()
    # loops_invoke()
    # f_string_invoke()
    # heaps_invoke()
    # deque_invoke()
    string_invoke()


if __name__ == "__main__":
    main()
