N = int(input())
countX = 0
countY = 0
for i in range(N):
  x,y = input().rstrip().split()
  countX += int(x)
  countY += int(y)
if countX > countY:
  print('Takahashi')
elif countY > countX:
  print('Aoki')
else:
  print('Draw')