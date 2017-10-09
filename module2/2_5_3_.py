x = [
    ("Guido", "van", "Rossum"),
    ("Haskel", "Curry"),
    ("John", "Backus")
]

def length(name):
    return len(" ".join(name))

name_length = [length(name) for i in x]
print(name_length)

x.sort(key=length)
print(x)

#
#
#
def length(name):
    return len(" ".join(name))

x.sort(key=lambda name: len(" ".join(name)))
print(x)
