import sys
args = sys.argv

index = int(arg[1])
new_animal = arg[2]

#動物の名前をリストに代入
animal = [
    "giraffe",
    "tiger",
    "zebra",
    "elephant",
    "lion",
]

#挿入
animal.insert(index, new_animal)

#リストの最後の要素を削除
del animal[-1]

#リストを昇順に並べる
animal.sort()

print(animal,end="")