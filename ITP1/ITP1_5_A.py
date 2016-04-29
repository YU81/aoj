# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
result = []
for line in input_lines:
    if line == "0 0":
        break
    h, w = [int(x) for x in line.rstrip().split(" ")]
    single_draw = "#" * w
    total_draw_list = [single_draw] * h
    total_draw = "\n".join(total_draw_list)
    result.append(total_draw + "\n")

print("\n".join(result))
