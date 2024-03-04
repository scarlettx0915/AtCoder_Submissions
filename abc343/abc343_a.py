import random

n,m = input().split()
a = int(n) + int(m)
out = random.choice([x for x in range(10) if x != a])
print(out)