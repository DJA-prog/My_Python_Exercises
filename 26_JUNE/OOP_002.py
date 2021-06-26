class Employee:
    """docstring for  employee."""
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # method
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@mail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
class Employee:
    """docstring for  employee."""
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # method
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@mail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corry', 'Roden', 6000)  # instance set
emp_2 = Employee('Lorry', 'Cart', 55000)  # instance set

print(emp_1.raise_amount)
print(Employee.raise_amount)


emp_1 = Employee('Corry', 'Roden', 6000)  # instance set
emp_2 = Employee('Lorry', 'Cart', 55000)  # instance set

print(emp_1.raise_amount)
print(Employee.raise_amount)
