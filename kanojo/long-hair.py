l = []
for i in range(5):
    p = input()
    l.append(p)


def f(l):
    return "yes" if l.count("yes") > l.count("no") else "no"


result = f(l)
print(result)
