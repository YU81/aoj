#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
match_count = int(input_lines.pop(0))
taro_point, hanako_point = 0, 0
WIN_POINT = 3
DRAW_POINT = 1
for line in input_lines:
    taro_card, hanako_card = line.rstrip().split(" ")
    if taro_card == hanako_card:
        taro_point += DRAW_POINT
        hanako_point += DRAW_POINT
        continue
    sorted_cards = sorted([taro_card, hanako_card], reverse=True)
    if sorted_cards[0] == taro_card:
        taro_point += WIN_POINT
        continue
    if sorted_cards[0] == hanako_card:
        hanako_point += WIN_POINT
        continue

print(taro_point, hanako_point)
