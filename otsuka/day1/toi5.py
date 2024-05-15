import sys 
args = sys.argv
args[1]=70
args[2]=70
args[3]=70
if args[1] >= 70 and args[2]>=70 and args[3]>=70:
    result = "合格"
if int(args[1])+int(args[2])+int(args[3])>=220 and args[1]>=50 and args[2]>=50 and args[3]>=50:
    result ="合格"
if args[1] <70 or args[2]<70 or args[3]<70:
    result ="不合格"
if args[1]<50 or args[2]<50 or args[3]<50:
    result ="不合格"
print(result)