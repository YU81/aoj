#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")

count = -1
threshold = -1
s = ""

for line in input_lines:
    if line == "-":
        break
    if count == -1:
        s = line
        count += 1
        continue
    if count == 0:
        threshold = int(line)
        count += 1
        continue

    shuffle_idx = int(line)
    s = s[shuffle_idx:] + s[:shuffle_idx]

    if count >= threshold:
        print(s)
        count = -1
        threshold = -1
        s = ""
        continue

    count += 1
