#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
target_str = input_lines.pop(0)
count = input_lines.pop(0)

for line in input_lines:
    fields = line.rstrip().split(" ")
    command = fields[0]
    a, b = (int(fields[1]), int(fields[2]))
    if command == "print":
        print(target_str[a:b + 1])
    elif command == "reverse":
        target_str = target_str[:a] + target_str[a:b + 1][::-1] + target_str[b + 1:]
    elif command == "replace":
        replace_str = fields[3]
        target_str = target_str[:a] + replace_str + target_str[b + 1:]
