S = input()
new = ''.join(sorted(S))
if new == S:
  print('Yes')
else:
  print('No')