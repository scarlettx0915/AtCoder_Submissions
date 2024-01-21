n = str(bin(int(input())))

def ctz(x):
    count = 0
    for i in reversed(x):
      if i == '0':
        count += 1
      else:
        return count
        
print(ctz(n))
    