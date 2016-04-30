#!/usr/bin/env python
# coding : utf-8
total_seconds = int(input())
hour = total_seconds // 3600
minutes = (total_seconds - 3600 * hour) // 60
seconds = (total_seconds - 3600 * hour - 60 * minutes)
print("{}:{}:{}".format(hour, minutes, seconds))
