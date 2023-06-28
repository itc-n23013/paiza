M, N = map(int, input().split())


def f(M, N):
    return 0 if M <= N else M - N


result = f(M, N)
print(result)
