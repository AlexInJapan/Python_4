import sys
args = sys.argv

a_file = open("sheep.txt", mode="w",encoding="utf-8")

num = int(args[1])

for i in range(1,num+1):
    a_file.write(f"ひつじが{i}匹\n")

a_file.close()

#ファイルを閉じる
with open("sheep.txt", encoding="utf-8") as f:
    s = f.read()
    print(s)