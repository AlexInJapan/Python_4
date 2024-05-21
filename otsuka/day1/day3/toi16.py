import sys
args = sys.argv

#土日判定
import datetime
today = datetime.datetime.now()
today.weekday()

def calc(otona,kodomo):
    otona = int(args[2])
    kodomo = int(args[3])
    if today.weekday() > 4:
        okane = (otona * 2000) + (kodomo * 1200)
    else:
        okane = (otona * 2400) + (kodomo * 1500)
    return okane
        
otona = int(args[2])
kodomo = int(args[3])

#結果を表示する
v = calc(otona, kodomo)
print(v,end="")