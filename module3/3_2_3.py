import re

#print(re.match)
#print(re.search)
#print(re.findall)
#print(re.sub)

# [] — можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) — метасимволы
# \d — [0-9]
# \D — [^0-9]
# \s — [ \t\n\r\f\v] — пробельные символы
# \S — ^\s
# \w — [a-zA-Z0-9_] — буквы + цифры + _
# \W — ^\w

pattern = r"a[abc]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
