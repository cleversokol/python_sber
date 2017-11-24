import re
import sys

pattern = re.compile(r'z.{3}z')

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)

#string = "zzxzz"
#string = "zzz"
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")
