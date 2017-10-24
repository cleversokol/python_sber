import re
import sys

pattern = re.compile(r'human')

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, "computer", line)
    print(line)

#string = "I need to understand the human mind"
#string = "humanity"
#
#if re.search(pattern, string) != None:
#    string = re.sub(pattern, "computer", string)
#    print(string)
#else:
#    print("no")
