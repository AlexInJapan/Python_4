#印税を計算する関数
def calc_royalty(plice, sales, per):
    rate = per / 100 #印税率（ここでは10）を100で割る
    ro = int(price * sales * rate) #定価と発行部数と印税率をかけて、それを整数にする
    return ro

#ユーザーから情報を入力してもらう
i = input("定価は？")
price = int(i)

i = input("印税率（パーセント）は？")
per = float(i)

#結果を表示する
v = calc_royalty(price, sales, per) #calc_royalty()関数を呼び出す
print("印税は、",v,"円です")