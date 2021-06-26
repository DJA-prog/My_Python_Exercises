class calc:
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def add(self):
        return self.val1 + self.val2

    def sub(self):
        return self.val1 - self.val2

    def multi(self):
        return self.val1 * self.val2

    def div(self):
        return self.val1 / self.val2