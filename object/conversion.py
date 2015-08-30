__author__ = 'stallon'


def to_int():
    s = '1234'
    f = 4.56
    l = 12345678909887655443433

    print(int(s), int(f), int(l))


def  to_other_sequences():
    t = (1, 2, 3, 4)
    l = [5, 6, 7, 8]
    s = 'abcd'

    print(list(t))
    print(tuple(l))
    print(tuple(s))


def list_tuple_dict():
    s = 'Python is one of the most famous language.'.split()
    keys = (1, 2, 3, 4, 5, 6, 7, 8)

    L = zip(keys, s)
    print(L)

    L = dict(L)
    print(L)

def main():

    to_int()
    to_other_sequences()
    list_tuple_dict()


if __name__ == '__main__':
    main()