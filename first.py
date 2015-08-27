# -*- coding: utf-8 -*-
__author__ = '홍성봉'

from decimal import *

s = 'module file sample'

def add(a, b):
    return a+b


def printLargeInteger():
    large_integer = 2**3**4
    print('Large Integer = %d' % large_integer)


def printStr(str):
    for c in str:
        print(c, end=' ')
    else:
        print()


def substract(a, b):
    return a-b


def main():
    print(add(3,4))
    printLargeInteger()
    printStr("stallon")
    print(substract(3,4))

    a = NewTest(1, 2, named=3)


class NewTest(object):

    def __new__(cls, *args, **kwargs):
        new_instance = super(NewTest, cls).__new__(cls, *args, **kwargs)
        return new_instance

    def __init__(self, a, b, **kwargs):
        print("__init__ gets called")
        print("a = {0}, b = {1} ".format(a, b))
        self.a = a
        self.b = b


if __name__ == '__main__':
    main()

