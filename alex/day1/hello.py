print("this is alex")

math = 49
japanese = 80
english = 91
sum = math+ japanese+english

import sys
args = sys.argv
 
kyuuyogaku = 1100000

if kyuuyogaku > 1000000:
    zeigaku =(round((kyuuyogaku-1000000) * 0.2 + 100000))
    sikyuugaku = (kyuuyogaku - zeigaku)
    print(f"支給額:{sikyuugaku}、税額:{zeigaku}",end="")
else:
    zeigaku = round(kyuuyogaku*0.1)
    sikyuugaku = kyuuyogaku - zeigaku
    print(f"支給額:{sikyuugaku}、税額:{zeigaku}",end="")



