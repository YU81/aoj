#!/usr/bin/env python
# coding : utf-8
strings = input().rstrip()
result = ""
for i in range(len(strings)):
    result += strings[i].upper() if strings[i].islower() else strings[i].lower()

print(result)
