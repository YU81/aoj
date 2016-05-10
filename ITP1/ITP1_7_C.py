#!/usr/bin/env python
# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
r, c = [int(x) for x in input_lines.pop(0).split(" ")]
rows = input_lines
# 2次元配列に展開
matrix = [[int(field) for field in row.rstrip().split(" ")] for row in rows]

# 各行の和
row_totals = [sum(row) for row in matrix]
# 各列の和
column_totals = [sum(col) for col in zip(*matrix)]

# 各行の和を各行末尾に追加
idx = 0
for row in matrix:
    row.append(row_totals[idx])
    idx += 1

# 表全体の和を計算
table_total = sum(row_totals)

# 各列の和を各列末尾に追加
# 末尾には表全体の和が入る
column_totals.append(table_total)
matrix.append(column_totals)

# 出力用に変換
result_matrix = [[str(field) for field in row] for row in matrix]
result = "\n".join([" ".join(row) for row in result_matrix])
print(matrix)
print(list(zip(*matrix)))
print(result)
