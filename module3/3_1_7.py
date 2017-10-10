#s = input()
#t = input()
#slen = len(s)
#tlen = len(t)
#count = 0
#if s.find(t) != -1:
#    for index in range(slen):
#        if s.find(t, index, index + tlen) != -1:
#            count += 1
#    print(count)
#else:
#    print(0)
s = input()
t = input()
slen = len(s)
tlen = len(t)
count = 0
if s.find(t) != -1:
    for index in range(slen):
        if s.find(t, index, index + tlen) != -1:
            count += 1
print(count)
