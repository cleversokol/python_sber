s = input()
a = input()
b = input()
count = 0
if b.find(a) != -1:  # if a is a substring of b, than substitution will be infinite
    if s.find(a) == -1:
        print(0)
    else:
        print("Impossible")
else:
    while s.find(a) != -1:
        s = s.replace(a, b)
        count += 1
    print(count)
