# coding : utf-8
a, b = [int(x) for x in input().rstrip().split(" ")]
quotient = a // b
remainder = a % b
float_quatient = a / b
print("%d %d %f" % (quotient, remainder, float_quatient))
