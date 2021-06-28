class Calcu:
    """This class use operators to supply a mathematical answer"""

    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def addition(self):
        return self.val1 + self.val2

    def subtraction(self):
        return self.val1 - self.val2

    def multiplication(self):
        return self.val1 * self.val2

    def division(self):
        return self.val1 / self.val2

    def power(self):
        return self.val1 ** self.val2

    def inverse(self):
        return 1 / self.val1
