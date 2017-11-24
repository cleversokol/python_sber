# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w﻿.

import re
import sys

pattern = re.compile(r'\b(\w)(\w)')

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r'\2\1', line)
    print(line)

#string = "this is a text"
#string = "\"this\' !is. ?n1ce,"
#
#if re.search(pattern, string) != None:
#    string = re.sub(pattern, r'\2\1', string, 1)
#    print(string)
#else:
#    print("no")