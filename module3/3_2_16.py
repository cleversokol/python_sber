import re
import sys

pattern = re.compile(r'\A((1(00)*1)+|((10){2,}1)+|0*)*\Z')

#for line in sys.stdin:
#    line = line.rstrip()
#    if re.match(pattern, line) != None:
#        print(line)
#    else:
#        print("no")

for i in range(1000):
    if i%3 == 0:
        string = "{0:b}".format(i)
        if re.search(pattern, string) == None:
        #    print(string)
        #else:
            print("no: ", string)

#string = input()
#if re.search(pattern, string) != None:
#        print(string)
#else:
#    print("no")

# 111000111101
# 001110110001
# 001110110100
# 001110110111
# 001110111010
# 001110111101
# 001111000000

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
#pattern = re.compile(r'\A\b((1(00)*1)+|((10){2,}1)+|0*)*\b\Z')

# если разница между суммой цифр, стоящих на четных позициях
# и суммой цифр на нечетных позициях - делится на 3,
# то и само число - также делится на 3'.
#
# знакопеременная сумма цифр должна делиться на $3$. Например, $75 = 1001011_{2}, 1-0+0-1+0-1+1 = 0$
# С точки зрения программы, работающей со строкой символов,
# можно попробовать переформулировать так:
# поделить строку на группы по две цифры справа налево
# (дополнить слева нулем, если число цифр нечетно),
# посчитать число групп "01" и вычесть из него число групп "10".
# Результат должен делиться на 3.