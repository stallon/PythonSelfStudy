'''
I'm spending time in learning a new language 'Python'.
This se
__author__ = 'stallon'
ction is to exercise python file module usages.
'''

import json
import os


class Employee:

    '''Employee class __doc__ string'''

    def __init__(self, name, salary, dept):

        '__init__ is described here...'

        self.name = name
        self.salary = salary
        self.dept = dept

    def getName(self):
        return self.name


def fileread():

    if os.path.exists('t.txt'):
        f = open('t.txt', 'r')
        lines = f.readlines()
        print(lines)
        f.close()
    else:
        print("can't find 't.txt'")


def replace(old, new):

    if os.path.exists('sample.txt'):
        f = open('sample.txt', 'r')

        newlines = []

        for line in f:
            newline = []
            words = line.split()
            for word in words:
                if word == old:
                    newline.append(new)
                else:
                    newline.append(word)
            newlines.append(' '.join(newline))

        f.close()

        f = open('replace.txt', 'w')
        f.write('\n'.join(newlines))
        f.close()


def main():

    s = """It's power: Python developers typically report
they are able to develop applications in a half
to a tenth the amount of time it takes them to do
the same work in such languages as C."""

    f = open('t.txt', 'w')
    f.write(s + '\n')

    emp1 = Employee('hong', 100000, 'a-flat')
    json.dump(emp1.__dict__, f)
    f.close()

    fileread()
    replace('show', 'SHOW')




if __name__ == '__main__':
    main()