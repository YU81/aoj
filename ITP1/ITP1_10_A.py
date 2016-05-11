#!/usr/bin/env python
# coding : utf-8
x1, y1, x2, y2 = [float(x) for x in input().rstrip().split(" ")]
print(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
