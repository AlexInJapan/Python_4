#掛け算を行うだけの関数を定義
def mul(a, b):
    '''掛け算を行う関数''' #docstringを設定
    return a * b

#定義した関数を使う
print(mul(2,3))
print(mul(10,3))

help(mul) #docstringを確認