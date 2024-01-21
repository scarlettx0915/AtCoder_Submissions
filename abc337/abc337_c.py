N = int(input())

Dict = {}
s = input().split()
for i in range(N):
  Dict[s[i]] = i+1
L = []
L.append(Dict['-1'])
for i in range(1,N):
  x = str(L[i-1])
  L.append(str(Dict[x]))

print(*L, sep = ' ')