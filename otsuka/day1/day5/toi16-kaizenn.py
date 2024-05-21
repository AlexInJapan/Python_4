import sys
args = sys.argv

#入力された日付が平日か土日かの判定を行う
import datetime
today = datetime.datetime.now()
today.weekday() #月曜日～日曜日を0～6の整数値で表す

#入場にかかる料金計算をする関数の定義
def calc(adult, child):
    #平日の場合
    if today.weekday() < 4: 
        money = (adult * 2000) + (child * 1200)
    
    #休日の場合
    else: 
        money = (adult * 2400) + (child * 1500)
    return money

adult = int(args[2])
child = int(args[3])

#結果を表示する
v = calc(adult, child)
print(v, end="")