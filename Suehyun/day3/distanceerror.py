import sys
args = sys.argv
spot_1 = args[1]
spot_2 = args[2]
answer = 0

dstnc_dict = {
  '東京':0.00,
  '品川':6.78,
  '新横浜':25.54,
  '名古屋':342.02,
  '京都':476.31,
  '新大阪':515.35
}

try:
  spot_1_from_toyko = dstnc_dict[spot_1]
  spot_2_from_toyko = dstnc_dict[spot_2]
  answer = abs(spot_1_from_toyko - spot_2_from_toyko)

  print(round(answer, 2), end='')
except:
  print('のぞみの停車駅を引数に設定してください',end='')