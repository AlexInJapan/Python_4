#支給額を計算する関数
def calcsalary(kyuuyogaku,zeigaku):
    kyuuyogaku = int(args[1])
if kyuuyogaku > 1000000:
    zeigaku =(round((kyuuyogaku-1000000) * 0.2 + 100000))
    sikyuugaku = (kyuuyogaku - zeigaku)
else:
    zeigaku = round(kyuuyogaku*0.1)
    sikyuugaku = kyuuyogaku - zeigaku

#ユーザーから情報を入力してもらう
i = input("給与は？")
kyuuyogaku = int(i)

#結果を表示する
v = calcsalary(kyuuyogaku,zeigaku) #calc()関数を呼び出す
print("支給額は、",v,"円です")