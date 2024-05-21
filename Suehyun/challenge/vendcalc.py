vend_products = {
  'お茶':110,
  'コーヒー':100,
  'ソーダ':160,
  'コーンポタージュ':130
}

def print_items():
  for key, value in vend_products.items():
    print(f'{key}：{value}円')

min_price = min(vend_products.values())

def insert_money():
  while True:
    payment = int(input('お金を投入してください：'))
    if (payment>10000):
      print('10,000円を超える金額は投入できません。再度投入金額を入力してください')
    elif (payment < min_price):
      print(f'{payment}円では購入できる商品がありません。再度投入金額を入力してください')
    elif (payment % 10 != 0):
      print('1円玉、5円玉は使用できません。再度投入金額を入力してください')
    else:
      break
  return payment

def ask_purchase():
  while True:
    product = input('何を購入しますか (商品名/cancel)：')
    if (product not in list(vend_products.keys())):
      print('該当する商品がありません。再度入力してください')
    else:
      break
  return product

print_items()
payment = insert_money()
product = ask_purchase()

# if (product != 'cancel'):
#   while (payment > 0):
#     print(f'残金：{payment - vend_products[product]}円')
#     payment -= vend_products[product]
#     re_purchase = input('続けて購入しますか (Y/N) ')
    
# print('おつり')