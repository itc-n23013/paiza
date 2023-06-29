N = int(input())
m = list(map(int, input().split()))


def f(N, m):
    return sorted(m)[N // 2]


result = f(N, m)
print(result)
