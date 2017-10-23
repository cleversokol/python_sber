import re
import sys

pattern = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)

#string = "catapult and cat"
#string = "!cat?"
#string = "\"cat\""
#string = "catcat"
#string = "Cat"
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")
