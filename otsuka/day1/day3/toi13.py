import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1] #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ") #果物類をタプルで定義
alcohol = ("ビール", "日本酒") #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
#入力されたもので分ける
if hm_class == "果物類":
    hm_class = fruits
    hinmoku["リンゴ"] = hinmoku["リンゴ"] - price_down
    hinmoku["みかん"] = hinmoku["みかん"] - price_down
    hinmoku["バナナ"] = hinmoku["バナナ"] - price_down

if hm_class == "酒類":
    hm_class = alcohol
    hinmoku["ビール"] = hinmoku["ビール"] - price_down
    hinmoku["日本酒"] = hinmoku["日本酒"] - price_down

if hm_class == "麺類":
    hm_class = noodles
    hinmoku["ラーメン"] = hinmoku["ラーメン"] - price_down
    hinmoku["うどん"] = hinmoku["うどん"] - price_down
    hinmoku["パスタ"] = hinmoku["パスタ"] - price_down

#値下げ後の金額が1円未満の場合は、1円とする。


#出力
print(hinmoku, end="")

if hm_class == "果物類":
    for fr in fruits:
        price = hinmoku[fr]-price_down
        if price <1:
            price = 1
        hinmoku[fr] = price

if hm_class == "酒類":
    for b in alcohol:
        price = hinmoku[b]-price_down
        if price <1:
            price = 1
        hinmoku[b] = price

if hm_class == "麺類":
    for c in noodles:
        price = hinmoku[c]-price_down
        if price <1:
            price = 1
        hinmoku[c] = price

print(hinmoku, end="")

