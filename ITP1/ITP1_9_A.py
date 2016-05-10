#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("END_OF_TEXT")[0].rstrip().lower().split("\n")
word = input_lines.pop(0)
target = (" ".join(input_lines).rstrip()).split(" ")
print(len([x for x in target if x == word]))
