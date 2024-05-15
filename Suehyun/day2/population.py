import sys
args = sys.argv
num = int(args[1])

ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
answer = ranking[num-1]

print(answer, end='')
