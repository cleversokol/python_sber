import re
import sys

pattern = re.compile(r'\\')

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)

#string = "\w denotes word character"
#string = "No slashes here"
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")
