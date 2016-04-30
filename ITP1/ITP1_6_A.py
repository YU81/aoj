# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
seq = input_lines[1].split(" ")
print(" ".join(seq[::-1]))
