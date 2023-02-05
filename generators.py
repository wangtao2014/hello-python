# Generators help you make lazy code.
def double_generator(iterable):
    for i in iterable:
        yield i + 1


def generator_to_list():
    values = (-x for x in [1, 2, 3, 4, 5])
    gen_to_list = list(values)
    print(gen_to_list)

