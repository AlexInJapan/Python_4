from datetime import date
import sys
args = sys.argv

def isWeekend(str):
  year = int(str[:4])
  month = int(str[4:6])
  day = int(str[6:])
  visit_date = date(year, month, day)
  return visit_date.isoweekday() > 5
  
def calcFee(isWeekend, adults, kids):
  if (isWeekend == True):
    print(f'{adults*2400 + kids*1500}', end='')
  else:
    print(f'{adults*2000 + kids*1200}', end='')

visit_date = args[1]
adults = int(args[2])
kids = int(args[3])

calcFee(isWeekend(visit_date), adults, kids)