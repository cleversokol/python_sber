def printab(a, b, **kwargs):
    print(a)
    print(b)
    for key in kwargs:
        print(key, kwargs[key])

printab(10, 20, c=30, d=40, jimmy=123)