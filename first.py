# -*- coding: utf-8 -*-
__author__ = '홍성봉'

from decimal import *

s = 'module file sample'

def add(a, b):
    return a+b


def printLargeInteger():
    large_integer = 2**3**4
    print('Large Integer = %d' % large_integer)


def main():
    print(add(3,4))
    printLargeInteger()
    printStr("stallon")



if __name__ == '__main__':
    main()

