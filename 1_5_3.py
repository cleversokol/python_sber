class Counter:
    def __init__(self, start=10):
        self.count = start
    # ключевое слово типа ??? в Scala
    pass

Counter
print(Counter)
x = Counter()
x1 = Counter(10)
print(x)
x.count = 0
x.count += 1