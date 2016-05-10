#!/usr/bin/env python
# coding : utf-8
import sys

alphabets = "abcdefghijklmnopqrstuvwxyz"
line = sys.stdin.read().rstrip().lower()
for x in alphabets:
    print("%s : %d" % (x, line.count(x)))
