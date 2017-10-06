class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.list = []

    def add(self, *a):
        # добавить следующую часть последовательности
        for arg in a:
            self.list.append(arg)
            if len(self.list) == 5:
                print(sum(self.list))
                self.list.clear()

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.list

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
print("----------------")
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
print("----------------")
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
print("----------------")
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]
print("----------------")
#            print("i = ", i, ", sum = ", sum)

###
# First one
#
#class Buffer:
#    def __init__(self):
#        # конструктор без аргументов
#        self.list = []
#
#    def add(self, *a):
#        # добавить следующую часть последовательности
#        for arg in a:
#            self.list.append(arg)
#        while len(self.list) > 4:
#            self.printSum()
#
#    def get_current_part(self):
#        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
#        return self.list
#
#    def printSum(self):
#        sum = 0
#        for i in range(5):
#            sum += self.list.pop(0)
#        print(sum)