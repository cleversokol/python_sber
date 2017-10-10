def simple_gen():
    print("checkpoint 1")
    yield 1
    print("checkpoint 2")
    yield 2
    print("checkpoint 3")

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)
