import sys
args = sys.argv

a = args[1]
b = a.split(" ")
c = int(args[2])
d = b[c-1]
print( d , end="")