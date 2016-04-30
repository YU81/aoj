#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
result = []
for line in input_lines:
    if line == "0 0":
        break
    h, w = [int(x) for x in line.rstrip().split(" ")]
    single_draw = "#" * w
    middle_single_draw = "#" + "." * (w - 2) + "#"
    total_draw_list = [single_draw] + [middle_single_draw] * (h - 2) + [single_draw]
    total_draw = "\n".join(total_draw_list)
    result.append(total_draw + "\n")

print("\n".join(result))
