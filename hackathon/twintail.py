s = int(input())
t = int(input())


def f(s, t):
    return "".join(["-" if i != t - 1 else "+" for i in range(s)])


result = f(s, t)
print(result)
