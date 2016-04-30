#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")

for line in input_lines:  # type:str
    if "?" in line:
        break
    a, op, b = line.split(" ")
    if op == "+":
        print(int(a) + int(b))
    elif op == "-":
        print(int(a) - int(b))
    elif op == "*":
        print(int(a) * int(b))
    elif op == "/":
        print(int(a) // int(b))
