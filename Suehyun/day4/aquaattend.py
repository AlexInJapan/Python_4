from datetime import date
from database import session
from tables import Attendnum
import sys

args = sys.argv

input_date = args[1]
adults = int(args[2])
kids = int(args[3])

visit_year = int(input_date[:4])
visit_month = int(input_date[4:6])
visit_day = int(input_date[6:])

visit_date = date(visit_year, visit_month, visit_day)

get_attend = session.query(Attendnum).filter_by(entry_date=visit_date).order_by(Attendnum.seq.desc()).first()

if get_attend != None:
  seq = get_attend.seq + 1
else:
  seq = 1

attendum = Attendnum(
  date = visit_date,
  seq = seq,
  adult = adults,
  child = kids
)

session.add(attendum)

session.commit()