#!/usr/bin/env python3


import asyncio
import time


# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


# 生产者
def produce(c):
    # TypeError: can't send non-None value to a just-started generator
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


async def hello():
    print('hello world')
    r = await asyncio.sleep(1)
    print('hello again!')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f'started at {time.strftime('%X')}')

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f'finished at {time.strftime('%X')}')


# Python对协程的支持是通过 generator 实现的
if __name__ == '__main__':
    # c = consumer()
    # print(c)
    # produce(c)
    asyncio.run(main())
