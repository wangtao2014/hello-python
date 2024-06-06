#!/usr/bin/env python3
# class inherit


class Animal(object):

    def run(self):
        print('Animal is running....')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


if __name__ == '__main__':
    animal = Animal()
    animal.run()

    dog = Dog()
    dog.run()
