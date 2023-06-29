n, m = map(int, input().split())
s = input()
t = input()


def func1(s, t):
    for c in s:
        if c in t:
            t = t.replace(c, "", 1)
    return len(t)


result = func1(s, t)
print(result)
