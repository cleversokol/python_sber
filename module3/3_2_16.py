import re
import sys

pattern = re.compile(r'\A\b((1(00)*1)+|((10){2,}1)+|0*)*\b\Z')

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) != None:
        print(line)
    else:
        print("no")


#string = input()
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")


# Chronological RE
#pattern = re.compile(r'((11)*0*)*|(1(00)*1)*')
#pattern = re.compile(r'(((1(00)*1)*)*0*)*')
#pattern = re.compile(r'\b((11)+0*|(1(00)+1)*)\b')
#pattern = re.compile(r'\b((11)+0*)\b')
#pattern = re.compile(r'\b((1(00)+1)+)0*\b')

#pattern = re.compile(r'\b(0|(1(00)*1)+0*)\b')
#pattern = re.compile(r'\b(0|((10){2,}1)+0*)\b')
#pattern = re.compile(r'\b(0|((1(00)*1)+|((10){2,}1)+)+0*)\b')

#pattern = re.compile(r'\A\b(0|0*((1(00)*1)+|((10){2,}1)+)+0*)\b\Z')
#pattern = re.compile(r'\A\b(0*((1(00)*1)+0*|((10){2,}1)+0*)*0*)\b\Z')
#pattern = re.compile(r'\A\b((1(00)*1)+|((10){2,}1)+|0*)*\b\Z')