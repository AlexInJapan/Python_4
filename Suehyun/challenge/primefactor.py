import sys
args = sys.argv

num = int(args[1])
prime_factors = []
i = 2

while i <= num:
  if (num%i==0):
    prime_factors.append(i)
    num = num/i
  else:
    i += 1

print(prime_factors, end='')