class Employee:
    """docstring for  employee."""

    def __init__(self, first, last, pay):  # method
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@mail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# basically emp_1 is the self placed into the class function.
emp_1 = Employee('Corry', 'Roden', '6000')  # instance
# emp_1.first = 'Corry'
# emp_1.last = 'Roden'
# emp_1.email = 'c.rodden@mail.com'
# emp_1.pay = '6000'
print(emp_1.email)  # print attribute
# print('{} {}'.format(emp_1.first, emp_1.last)) # Corry Roden
print(emp_1.fullname())  # print attribute
print(Employee.fullname(emp_1))  # print attribute


emp_2 = Employee('Lorry', 'Cart', '55000')  # instance
print(emp_2.email)  # print attribute
