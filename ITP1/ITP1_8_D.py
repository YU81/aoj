#!/usr/bin/env python
# coding : utf-8
s, p = input(), input()
s = s * int(1 + 100 // len(s))
print("Yes" if p in s else "No")
