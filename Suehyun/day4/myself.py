from introduce import *
import sys
args = sys.argv

person = Intro(args[1], args[2])

print(person.name_out())
print(person.age_out())