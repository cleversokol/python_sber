class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.capacity >= v

    def add(self, v):
        # положить v монет в копилку
        self.capacity -= v
