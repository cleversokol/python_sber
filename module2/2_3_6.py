x = [-2, -1, 0, 1, 2]
y = []
for i in x:
    y.append(i * i)


# the same for y
y = [i*i for i in x]
z = [(x, y) for x in range(3) for y in range(3) if x <= y]
print(z)

z = ((x, y) for x in range(3) for y in range(3) if x <= y)
print(z)
print(next(z))
print(next(z))
