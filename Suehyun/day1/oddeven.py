import sys
args = sys.argv
input = int(args[1])

if (input % 2 == 0):
  print('偶数', end='')
else:
  print('奇数', end='')