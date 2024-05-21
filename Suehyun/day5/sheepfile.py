import sys
args = sys.argv

n = int(args[1])

with open('sheep.txt', mode='w', encoding='utf-8') as file:
  for i in range(n):
    file.write(f'ひつじが{i+1}匹 \n')

with open('sheep.txt', encoding='utf-8') as file:
  output = file.read()
  print(output)