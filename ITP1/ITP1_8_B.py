#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")

for line in input_lines:
    if line == "0": break
    print(sum([int(x) for x in line]))
