def iter_with_index():
    animals = ["dog", "cat", "mouse"]
    for i, value in enumerate(animals):
        print(i, value)   # 0 dog 1 cat 2 mouse


def range_loop():
    for value in range(9):  # range(4, 8)  range(4, 10, 2)
        print(value)


def zip_loop():
    words = ['Mon', 'Tue', 'Wed']
    nums = [1, 2, 3]
    # Use zip to pack into a tuple list
    for w, n in zip(words, nums):
        print('%d:%s, ' % (n, w))


def else_loop():
    nums = [50, 70, 30, 100, 110]
    for n in nums:
        if n > 200:
            print("%d is bigger than 100" % n)
            break
    else:  # https://book.pythontips.com/en/latest/for_-_else.html 没有走到 break 的情况下执行
        print("Not found!")
