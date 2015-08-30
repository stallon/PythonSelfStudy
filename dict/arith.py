# -*- coding: utf-8 -*-
__author__ = 'stallon'

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def choose_menu():
    print('무엇을 하고 싶나요 - add, sub, mul, div, quit')
    return input('당신의 선택은? ')


def main():
    menu = { 'add':add, 'sub': sub, 'mul': mul, 'div': div}
    choice = choose_menu()

    while choice != 'quit':
        if choice in menu:
            x = int(input('첫번째 값: '))
            y = int(input('두번째 값: '))
            print('결과 = ', menu[choice](x, y))

        choice = choose_menu()


if __name__ == '__main__':
    main()

