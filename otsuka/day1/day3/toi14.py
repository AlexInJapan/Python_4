import sys
args = sys.argv

#３つの整数を入力し、それぞれ奇数ならば「ｘは奇数」、偶数ならば「ｘは偶数」と表示するプログラムを作成する
#なお、プログラム中に、計算と結果の出力を処理する関数calcvalueを作成し、使用すること

#calcvalue関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

#情報を入力してもらう
for i in range(1,4,1):
    num = int(args[i])
    v = calcvalue(num)