#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")

for line in input_lines:
    if line == "0 0":
        break
    numbers = [int(x) for x in line.rstrip().split(" ")]
    numbers.sort()
    result = [str(x) for x in numbers]
    print(" ".join(result))
