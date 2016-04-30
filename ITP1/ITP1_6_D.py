# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
row_count, col_count = [int(x) for x in input_lines.pop(0).split(" ")]
matrix = [[0 for y in range(col_count)] for x in range(row_count)]

for i in range(row_count):
    numbers = [int(x) for x in input_lines.pop(0).split(" ")]
    matrix[i] = numbers

vector = [int(x) for x in input_lines]

result_vector = []
for i in range(row_count):
    elem = 0
    for j in range(col_count):
        elem += matrix[i][j] * vector[j]
    result_vector.append(elem)

print("\n".join([str(x) for x in result_vector]))
