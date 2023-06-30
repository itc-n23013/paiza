n = int(input())
l = [] * n


def f(n):
    for i in range(n, -1, -1):
        l.append("0!!" if i == 0 else str(i))
    return "\n".join(l)


result = f(n)
print(result)
