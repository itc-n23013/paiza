n = int(input())
s = [input() for _ in range(n)]


def f(n, s):
    return "_".join(s)


result = f(n, s)
print(result)
