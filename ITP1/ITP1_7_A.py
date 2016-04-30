# coding : utf-8
import sys


def judge(m, f, r):
    """
    :param int m:
    :param int f:
    :param int r:
    :rtype str:
    """
    if m == -1 or f == -1:
        return "F"
    total = m + f
    if total >= 80:
        return "A"
    if 65 <= total <= 80:
        return "B"
    if 50 <= total < 65:
        return "C"
    if 30 <= total < 50:
        if r >= 50:
            return "C"
        return "D"
    return "F"


input_lines = sys.stdin.read().rstrip().split("\n")

scores = [[int(y) for y in x.split(" ")] for x in input_lines]
judges = [judge(z[0], z[1], z[2]) for z in scores if z != [-1, -1, -1]]
print("\n".join(judges))
