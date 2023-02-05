import heapq  # https://docs.python.org/3/library/heapq.html


def heap_create():
    my_list = [9, 5, 4, 1, 3, 2]
    heapq.heapify(my_list)   # turn myList into a Min Heap
    print(my_list)
    print(my_list[0])

    heapq.heappush(my_list, 10)  # insert 10
    x = heapq.heappop(my_list)  # pop and return smallest item
    print(x)


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
