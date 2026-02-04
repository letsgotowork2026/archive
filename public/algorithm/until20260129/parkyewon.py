n = int(input())

d = [5001] * (n + 1)
d[0] = 0

for i in range(1, n + 1):
    if i >= 3:
        d[i] = min(d[i], d[i - 3] + 1)
    if i >= 5:
        d[i] = min(d[i], d[i - 5] + 1)

if d[n] != 5001:
    print(d[n])
else:
    print("-1")