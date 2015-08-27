# -*- coding: utf-8 -*-
__author__ = '홍성봉'

from decimal import *

s = 'module file sample'

def add(a, b):
    return a+b


def printLargeInteger():
    large_integer = 2**3**4
    print('Large Integer = %d' % large_integer)


def substract(a, b):
    return a-b


def main():
    print(add(3,4))
    printLargeInteger()
    print(substract(3,4))


if __name__ == '__main__':
    main()

