# coding : utf-8
import sys

input_lines = sys.stdin.read().rstrip().split("\n")
result = []
for line in input_lines:
    if line == "0 0":
        break
    h, w = [int(x) for x in line.rstrip().split(" ")]

    hash_first_draw = ("#." * (1 + w // 2))[:w]
    dot_first_draw = (".#" * (1 + w // 2))[:w]

    total_draw_list = []
    is_hash_first = True
    for i in range(h):
        if is_hash_first:
            total_draw_list.append(hash_first_draw)
        else:
            total_draw_list.append(dot_first_draw)

        is_hash_first = not is_hash_first

    total_draw = "\n".join(total_draw_list)
    result.append(total_draw + "\n")

print("\n".join(result))
