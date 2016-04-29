# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")

cnt = 1
for line in input_lines:
    if line == "0":
        break
    print("Case {}: {}".format(cnt, line))
    cnt += 1
