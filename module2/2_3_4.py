class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos > 0

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.index = 0
        self.judge = judge
        self.funcs = []
        for f in funcs:
            self.funcs.append(f)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self
    
    def __next__(self):
        while True:
            pos = 0
            neg = 0
            if self.index < len(self.iterable):
                i = self.iterable[self.index]
                self.index += 1
                for f in self.funcs:
                    if f(i):
                        pos += 1
                    else:
                        neg += 1
                if self.judge(pos, neg):
                    return i
            else:
                raise StopIteration


#
#
#
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
