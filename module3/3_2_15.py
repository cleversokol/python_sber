import re
import sys

pattern = re.compile(r'(\w)\1+')

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r'\1', line)
    print(line)

#string = "attraction"
#string = "buzzzz"
#
#if re.search(pattern, string) != None:
#    string = re.sub(pattern, r'\1', string)
#    print(string)
#else:
#    print("no")