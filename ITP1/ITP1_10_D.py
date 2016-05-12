#!/usr/bin/env python
# coding : utf-8
import sys
import math


def distance(v1, v2, p):
    dimensions = (len(v1), len(v2))
    if dimensions[0] != dimensions[1]:
        return -1

    result = 0
    if p < float('inf'):
        for i in range(dimensions[0]):
            result += math.fabs(v1[i] - v2[i]) ** p
        result = result ** (1 / p)
    else:
        each_distance = []
        for i in range(dimensions[0]):
            each_distance.append(math.fabs(v1[i] - v2[i]))
        result = max(each_distance)

    return result


input_lines = sys.stdin.read().rstrip().split("\n")
dimension = int(input_lines.pop(0))
vectors = [[float(x) for x in line.rstrip().split(" ")] for line in input_lines]
print(distance(vectors[0], vectors[1], 1))
print(distance(vectors[0], vectors[1], 2))
print(distance(vectors[0], vectors[1], 3))
print(distance(vectors[0], vectors[1], float('inf')))
