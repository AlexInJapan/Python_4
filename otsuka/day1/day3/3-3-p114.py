#リスト要素を結合して文字列にする
"連結文字".join(リストなど)

a = ["aaa" , "bbb" , "ccc"]
"-".join(a) #aaa-bbb-cccが出力

#文字列を分割
s = "2020/02/20"
a = s.split("/")
a #変数aの内容を表示。2020 , 02 , 20 が出力。
#分割したリストを結合
s = "-".join(a)
#変数sの内容を表示
s #2020-02-20が出力

#文字列の置換
str.replace(old, new [.count])

s = "This is a pen"
s.replace("pen" , "note") #replace()の結果を確認。This is a noteを出力
s #sの値は変更されていないことを確認。This is a penを出力