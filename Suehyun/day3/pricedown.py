import sys
args = sys.argv

cate = args[1]
price_down = int(args[2])

products_dict = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

fruits = ("リンゴ", "みかん", "バナナ")
alcohol = ("ビール", "日本酒")
noodles = ("ラーメン", "うどん", "パスタ")

if cate == '果物類':
  for fruit in fruits:
    products_dict[fruit] -= price_down
elif cate == '酒類':
  for liquor in alcohol:
    products_dict[liquor] -= price_down
else:
  for noodle in noodles:
    products_dict[noodle] -= price_down

for key in products_dict.keys():
  if (products_dict[key] < 1):
    products_dict[key] = 1

print(products_dict, end='')