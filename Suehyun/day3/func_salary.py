def calcsalary(pre_tax):
  after_tax = 0
  tax = 0

  if (pre_tax <= 1000000):
    tax = pre_tax*0.1
  else:
    tax = (pre_tax-1000000)*0.2 + 100000

  tax = round(tax)
  after_tax = pre_tax - tax
  print(f'支給額:{after_tax}、税額:{tax}')