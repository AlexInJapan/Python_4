from func_salary import calcsalary
import sys

args = sys.argv

for arg in args[1:]:
  calcsalary(int(arg))
