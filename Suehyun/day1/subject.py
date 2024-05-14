import sys
args = sys.argv
math_result = int(args[1])
japanese_result = int(args[2])
english_result = int(args[3])
output = ''

if (math_result >= 50) and (japanese_result >= 50) and (english_result >= 50):
  if (math_result+japanese_result+english_result) >= 220:
    output = '合格'
  else:
    if (math_result >= 70) and (japanese_result >= 70) and (english_result >= 70):
      output = '合格'
    else:
      output = '不合格'
else:
  output = '不合格'

print(output, end='')