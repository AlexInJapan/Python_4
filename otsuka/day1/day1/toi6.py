import sys
args = sys.argv

kyuuyogaku = int(arg[1])
if kyuuyogaku > 1000000:
    zeigaku = int((kyuuyogaku-1000000) * 0.2 + 100000)
    sikyuugaku = kyuuyogaku - zeigaku
else:
    zeigaku = int(kyuuyogaku*0.1)
    sikyuugaku = kyuuyogaku - zeigaku
print(f"支給額:"{sikyuugaku}"、税額:"{zeigaku},end="")