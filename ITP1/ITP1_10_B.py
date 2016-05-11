#!/usr/bin/env python
# coding : utf-8
from math import sin, cos, pi

a, b, c = [float(x) for x in input().rstrip().split(" ")]
# 角度を度数法からラジアンに変換
theta_in_radian = c * pi / 180.0

# 面積 = (1/2) * a * b * sin(c)
s = 0.5 * a * b * sin(theta_in_radian)

# 辺xの長さの2乗 = aの2乗 + bの2乗 - 2 * a * b * cos(c)
# 周の長さ = a + b + x
x = (a ** 2 + b ** 2 - 2 * a * b * cos(theta_in_radian)) ** 0.5
l = a + b + x

# 三角形の面積 = 底辺 * 高さ / 2
h = 2 * s / a

print(s)
print(l)
print(h)
