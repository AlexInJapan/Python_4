from datetime import date
from database import session
from tables import Holiday
import sys

args = sys.argv

input_date = args[1]
adults = int(args[2])
kids = int(args[3])

visit_year = int(input_date[:4])
visit_month = int(input_date[4:6])
visit_day = int(input_date[6:])

visit_date = date(visit_year, visit_month, visit_day)
fee = 0

def calc_fee(date, adults, kids):
  if visit_date.isoweekday() > 5:
    fee = adults*2400 + kids*1500
  else:
    get_date = session.query(Holiday.holi_date).filter_by(holi_date=date).first()
    if get_date is None:
      fee = adults*2000 + kids*1200
    else:
      fee = adults*2400 + kids*1500
  return fee

print(f'{calc_fee(visit_date, adults, kids)}円')