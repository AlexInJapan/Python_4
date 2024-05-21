#BMI判定（例外処理あり版）
#ユーザーから正しい値を得てBMIを計算
while True:
    try: #breakするまで繰り返す
        #入力
        weight = float(input("体重（㎏）は？"))
        height = float(input("身長（㎝）は？"))
        #BMIの計算
        height = height / 100 #mに直す
        bmi = weight / (height * height)
        break:
    except:
        print("入力ミスがあります。再度入力してください。")

#bmi の値から結果を判定
result = ""
if bmi < 18.5: result = "瘦せ型"
elif bmi < 25: result = "標準体型"
elif bmi < 30: result = "肥満（軽）"
else: result = "肥満（重）"

#結果を表示
print("BMI:", bmi)
print("判定:", result)