#!/usr/bin/env python
# coding : utf-8
import sys
import itertools

mark_order = {"S": 1, "H": 2, "C": 3, "D": 4}


class CardInfo(object):
    def __init__(self, mark, number):
        self.mark = mark
        self.number = int(number)
        global mark_order

    def __eq__(self, other):
        return self.is_mark_equals(other) and self.number == other.number

    def __lt__(self, other):
        if self.is_mark_greater(other):
            return True
        elif self.is_mark_less(other or self.is_mark_equals(other)):
            return False
        else:
            return self.number < other.number

    def __gt__(self, other):
        if self.is_mark_less(other):
            return True
        elif self.is_mark_greater(other) or self.is_mark_equals(other):
            return False
        else:
            return self.number > other.number

    def __repr__(self):
        return "{} {}".format(self.mark, self.number)

    def __hash__(self):
        return hash(self.mark + str(self.number))

    def is_mark_greater(self, other):
        return mark_order[self.mark] < mark_order[other.mark]

    def is_mark_less(self, other):
        return mark_order[self.mark] > mark_order[other.mark]

    def is_mark_equals(self, other):
        return self.mark == other.mark


input_lines = sys.stdin.read().rstrip().split("\n")
input_lines.pop(0)
card_info_list = set([CardInfo(y[0], y[1]) for y in [x.split(" ") for x in input_lines]])
all_card_info_list = set(
    [CardInfo(mark, number) for mark, number in itertools.product(["S", "H", "D", "C"], range(1, 14))])
missing_list = all_card_info_list.difference(card_info_list)

for x in sorted(missing_list):
    print(x)
