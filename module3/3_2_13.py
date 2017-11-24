# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
import re
import sys

pattern = re.compile(r'\b[Aa]+\b')

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        line = re.sub(pattern, "argh", line, 1)
        print(line)

#string = "There’ll be no more ""Aaaaaaaaaaaaaaa"""
#string = "AaAaAaA AaAaAaA"
#
#if re.search(pattern, string) != None:
#    string = re.sub(pattern, "argh", string, 1)
#    print(string)
#else:
#    print("no")
