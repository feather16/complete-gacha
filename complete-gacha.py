import random

N = 3
T = 1000000
result = {}

for t in range(T):
    count = 0
    got = [False] * N
    while False in got:
        got[random.randrange(N)] = True
        count += 1
    if count not in result:
        result[count] = 0
    result[count] += 1

sum_count = 0
for n, count in sorted(result.items(), key=lambda x: x[0]):
    print(n, count / T, (sum_count + count) / T)
    sum_count += count