# coding : utf-8
l = [int(x) for x in input().rstrip().split(" ")]
result = [str(x) for x in sorted(l)]
print(" ".join(result))
