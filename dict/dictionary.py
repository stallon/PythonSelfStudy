# -*- coding: utf-8 -*-
__author__ = 'stallon'

def print_menu():
    print('1. 전화 번호 출력')
    print('2. 전화 번호 추가')
    print('3. 전화 번호 삭제')
    print('4. 전화 번호 찾기')
    print('5. 종료')
    print()


def print_dic(numbers):
    print('전화 번호 표시')
    for name in numbers:
        print('이름: %s \t 번호: %s' % (name, numbers[name]))
    print()


def add_member(numbers):
    print('이름과 번호 추가')
    name = input('이름: ')
    phone = input('번호: ')
    numbers[name] = phone


def remove_member(numbers):
    print('이름과 번호 삭제')
    name = input('이름: ')
    if name in numbers:
        del numbers[name]
    else:
        print('%s는 전화 번호부에 없습니다.' % name)


def lookup_member(numbers):
    print('번호 찾기')
    name = input('이름: ')
    if name in numbers:
        print('번호: %s', numbers[name])
    else:
        print('%s를 찾을 수 없습니다.' % name)


def main():
    numbers = {}
    menu_choice = ''
    print_menu()

    while menu_choice != '5':
        menu_choice = input('번호를 입력해 주세요 (1-5): ')
        if menu_choice == '1':
            print_dic(numbers)
        elif menu_choice == '2':
            add_member(numbers)
        elif menu_choice == '3':
            remove_member(numbers)
        elif menu_choice == '4':
            lookup_member(numbers)
        elif menu_choice != '5':
            print_menu()


if __name__ == '__main__':
    main()

