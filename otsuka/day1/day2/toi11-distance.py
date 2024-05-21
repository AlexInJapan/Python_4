import sys
args = sys.argv

#辞書データを作成
eki = { '東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

#計算
x = float(eki[args[1]])
y = float(eki[args[2]])

w = abs(y - x)

#小数点第二位まで出力
round(w,2)
print(w,end="")