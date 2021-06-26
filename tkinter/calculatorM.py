class Calcu:
    """This class use operators to supply a mathematical answer"""

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def addition(self, val1, val2):
        return val1 + val2

    def subtraction(self, val1, val2):
        return val1 - val2

    def multiplication(self, val1, val2):
        return val1 * val2

    def division(self, val1, val2):
        return val1 / val2

    def power(self, val1, val2):
        return val1 ** val2

    def inverse(self, val1):
        return 1 / val1
