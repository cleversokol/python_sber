import re
import sys

pattern = re.compile(r'\b(.+)\1\b')

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)

#string = "blabla is a tandem repetition"
#string = "123123 is good too"
#string = "go go"
#string = "aaa"
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")
