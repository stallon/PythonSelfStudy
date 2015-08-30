# -*- coding: utf-8 -*-
__author__ = 'stallon'

from operator import itemgetter


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def __tuple__(self):
        return (self.name, self.grade, self.age)

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)


DAVE = Student('dave', 'B', 10)
JOHN = Student('john', 'A', 15)
JANE = Student('jane', 'B', 12)
students = [DAVE, JOHN, JANE]
students_tuple = [DAVE.__tuple__(), JOHN.__tuple__(), JANE.__tuple__()]


def main():
    print(sorted(students, key=lambda student: student.grade))
    print(sorted(students_tuple, key=itemgetter(2)))



if __name__ == '__main__':
    main()
