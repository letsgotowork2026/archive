n = int(input())

d = [0] * (n + 1)
for i in range(n):
    d[i] = float(input())
    d[i] = max(d[i], d[i] * d[i - 1])


print('%.3f' % max(d))