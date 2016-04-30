#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
house = [[[0 for k in range(10)] for j in range(3)] for i in range(4)]
line_count = int(input_lines.pop(0))

for line in input_lines:
    building, flr, room, member_diff = [int(x) - 1 for x in line.split(" ")]
    member_diff += 1
    house[building][flr][room] += member_diff

for b in range(4):
    for f in range(3):
        print(" " + " ".join([str(r) for r in house[b][f]]))
    if b == 3:
        break
    print("####################")
