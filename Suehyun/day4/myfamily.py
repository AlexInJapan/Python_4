from intro_family import *
import sys
args = sys.argv

new_family = IntroFamily(args[1], args[2], args[3])

print(new_family.name_out())
print(new_family.age_out())
print(new_family.cat_out())