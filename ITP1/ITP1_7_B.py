# coding : utf-8
import sys
import itertools


def sum_condition_pair_count(n, x, combination=3):
    return len([y for y in itertools.combinations(range(1, n + 1), r=combination) if sum(y) == x])


input_lines = sys.stdin.read().rstrip().split("\n")

for line in input_lines:
    if line == "0 0":
        break
    n, x = [int(y) for y in line.split(" ")]
    print(sum_condition_pair_count(n, x))
