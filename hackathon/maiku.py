import math

n = int(input())
m = int(input())


def f(n, m):
    return math.ceil(m / (n * 2))


result = f(n, m)
print(result)
