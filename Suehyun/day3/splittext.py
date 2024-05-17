import sys
args = sys.argv
str = args[1]
num = int(args[2])

splitted_arr = str.split(' ')
answer = splitted_arr[num-1]

print(answer, end='')