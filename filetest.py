__author__ = 'stallon'

import json

'''
I'm spending time in learning a new language 'Python'.
This section is to exercise python file module usages.
'''

class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def getName(self):
        return self.name


def main():

    s = """It's power: Python developers typically report
they are able to develop applications in a half
to a tenth the amount of time it takes them to do
the same work in such languages as C."""

    f = open('t.txt', 'w')
    f.write(s)

    emp1 = Employee('hong', 100000, 'a-flat')
    json.dump(emp1.__dict__, f)
    f.close()




if __name__ == '__main__':
    main()