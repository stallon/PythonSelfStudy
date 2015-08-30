__author__ = 'stallon'

import copy


def shallow_copy():

    print('------ Shallow Copy ------')
    a = [1, 2, 3]
    b = [4, 5, a]
    x = [a, b, 100]
    y = x.copy()

    x.remove(100)
    print('x = ', x)
    print('y = ', y)

    a.append(4)
    print('x = ', x)
    print('y = ', y)
    print('------- End of Shallow Copy -----')


def deep_copy():
    print('------ Deep Copy ------')
    a = [1, 2, 3]
    b = [4, 5, a]
    x = [a, b, 100]
    y = copy.deepcopy(x)

    x.remove(100)
    print('x = ', x)
    print('y = ', y)

    a.append(4)
    print('x = ', x)
    print('y = ', y)
    print('------- End of Deep Copy -----')


def main():
    a = 1
    b = a
    print('a = {}, b = {}'.format(a, b))

    b = 3
    print('a = {}, b = {}'.format(a, b))

    shallow_copy()
    deep_copy()


if __name__ == '__main__':
    main()