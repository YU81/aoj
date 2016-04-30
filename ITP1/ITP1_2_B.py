#!/usr/bin/env python
# coding : utf-8
a, b, c = [int(x) for x in input().rstrip().split(" ")]
if a < b < c:
    print("Yes")
else:
    print("No")
