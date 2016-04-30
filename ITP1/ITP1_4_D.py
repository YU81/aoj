#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
numbers = [int(x) for x in input_lines[1].rstrip().split(" ")]
print(min(numbers), max(numbers), sum(numbers))
