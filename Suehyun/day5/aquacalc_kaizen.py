# Order of import
# Standard library - Related third party - Local application/library
import sys
from datetime import date

menus = {
  #weekend menu
  'weekend':
  {
  'adult': 2400,
  'child': 1500
  },
  #weekdays menu
  'weekdays':
  {
  'adult':2000,
  'child':1200
  }
}

# Extract list of arguments from the argv of the sys
args = sys.argv

class Aquarium:
  def __init__(self, date_str, adults, children):
    self.date_str = date_str
    self.adults = adults
    self.children = children

  # naming style: lower_case_with_underscores
  def is_weekend(self):
    '''
    When you give 8 letters str of date(e.g. '20220521') as argument,
    this function will return whether the date is weekend or not.
    If the visit is on weekends, this function will return True.
    If the visit is on weekdays, this function will return False.
    '''
    year = int(self.date_str[:4])
    month = int(self.date_str[4:6])
    day = int(self.date_str[6:])
    visit_date = date(year, month, day)
    return visit_date.isoweekday() > 5

  def calc_fee(self, is_weekend):
    '''
    This Function calculates admission fees for aquarium
    according to whether the visit is on weekdays or weekends.
    isWeeken = type boolean, adults = type int, children = type int
    '''
    if (is_weekend):
      return self.adults*menus['weekend']['adult'] + self.children*menus['weekend']['child']
    else:
      return self.adults*menus['weekdays']['adult'] + self.children*menus['weekdays']['child']

visit_date = args[1]
adults = int(args[2])
children = int(args[3])

data = Aquarium(visit_date, adults, children)
is_weekend = data.is_weekend()

# print admission fee
print(data.calc_fee(is_weekend), end='円\n')

