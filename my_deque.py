# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def deque_create():
    q = deque()  # create an empty deque
    q = deque([1, 2, 3])  # make a new deque with three items

    q.append(4)  # add a new entry to the right side
    q.appendleft(0)  # add a new entry to the left side

    print(q)  # deque([0, 1, 2, 3, 4])

    x = q.pop()  # remove & return from right
    y = q.popleft()  # remove & return from left
    print(x)  # => 4
    print(y)  # => 0
    print(q)  # => deque([1, 2, 3])

    q.rotate(1)  # rotate 1 step to the right
    print(q)  # => deque([3, 1, 2])
