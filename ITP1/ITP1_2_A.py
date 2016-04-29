# coding : utf-8
a, b = [int(x) for x in input().rstrip().split(" ")]
sign = "=="
if a < b:
    sign = "<"
elif a > b:
    sign = ">"

print("a {} b".format(sign))
