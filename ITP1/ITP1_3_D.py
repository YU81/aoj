# coding : utf-8
a, b, c = [int(x) for x in input().rstrip().split(" ")]
divisors = [x for x in range(a, b + 1) if c % x == 0]
print(len(divisors))
