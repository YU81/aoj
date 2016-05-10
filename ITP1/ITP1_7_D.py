#!/usr/bin/env python
# coding : utf-8
import sys


class Matrix(object):
    def __init__(self, row_count, col_count):
        self.rows = [[0 for y in range(col_count)] for x in range(row_count)]

    def __add__(self, other):
        """
        行列の加算。単純に各要素を足した新しい行列を返す。
        :param Matrix other:
        """
        if self.row_count() != other.row_count():
            raise ValueError
        if self.col_count() != other.col_count():
            raise ValueError
        new_matrix = Matrix(self.row_count(), self.col_count())
        new_matrix.rows = [[self.rows[row_idx][col_idx] + other.rows[row_idx][col_idx]
                            for col_idx in range(self.col_count())]
                           for row_idx in range(self.row_count())]
        return new_matrix

    def row_count(self):
        return len(self.rows)

    def col_count(self):
        return len(list(zip(*self.rows)))

    def __mul__(self, other):
        """
        行列の積を求め、結果の新しい行列を返す。
        :param Matrix other:
        """
        if self.col_count() != other.row_count():
            raise ValueError
        new_col_count = other.col_count()
        new_row_count = self.row_count()
        new_matrix = Matrix(new_row_count, new_col_count)

        for col_idx in range(new_col_count):
            for row_idx in range(new_row_count):
                new_element = 0
                for k in range(self.col_count()):
                    new_element += self.rows[row_idx][k] * other.rows[k][col_idx]
                new_matrix.rows[row_idx][col_idx] = new_element

        return new_matrix

    def __repr__(self):
        return "\n".join([" ".join([str(element) for element in fields]) for fields in self.rows])


input_lines = sys.stdin.read().rstrip().split("\n")

n, m, l = [int(x) for x in input_lines.pop(0).rstrip().split(" ")]

first_matrix = Matrix(n, m)

for i in range(n):
    line = input_lines.pop(0)
    elements = [int(x) for x in line.rstrip().split(" ")]
    first_matrix.rows[i] = elements

second_matrix = Matrix(m, l)
for j in range(m):
    line = input_lines.pop(0)
    elements = [int(x) for x in line.rstrip().split(" ")]
    second_matrix.rows[j] = elements

print(first_matrix * second_matrix)
